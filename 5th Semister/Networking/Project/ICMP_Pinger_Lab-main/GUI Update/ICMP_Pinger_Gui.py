import os
import struct
import time
import select
import socket
import threading
import tkinter as tk
from tkinter import messagebox

ICMP_ECHO_REQUEST = 8

# Ping functions
def checksum(data):
    csum = 0
    countTo = (len(data) // 2) * 2
    count = 0

    while count < countTo:
        thisVal = data[count + 1] * 256 + data[count]
        csum += thisVal
        csum &= 0xFFFFFFFF
        count += 2

    if countTo < len(data):
        csum += data[len(data) - 1]
        csum &= 0xFFFFFFFF

    csum = (csum >> 16) + (csum & 0xFFFF)
    csum += (csum >> 16)
    answer = ~csum & 0xFFFF
    answer = answer >> 8 | (answer << 8 & 0xFF00)
    return answer

def receiveOnePing(mySocket, ID, timeout, destAddr):
    timeLeft = timeout
    while True:
        startedSelect = time.time()
        whatReady = select.select([mySocket], [], [], timeLeft)
        howLongInSelect = (time.time() - startedSelect)
        if whatReady[0] == []:  # Timeout
            return None

        timeReceived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)

        # Fetch the ICMP header from the IP packet
        icmpHeader = struct.unpack('bbHHh', recPacket[20:28])
        type, code, checksum, packetID, sequence = icmpHeader

        if type != 0:
            return None
        if code != 0:
            return None
        if ID != packetID:
            return None

        send_time, = struct.unpack('d', recPacket[28:])
        rtt = (timeReceived - send_time) * 1000

        # Extract additional information from the IP header
        ipHeader = struct.unpack('!BBHHHBBH4s4s', recPacket[:20])
        ttl = ipHeader[5]  # Time-to-live
        saddr = socket.inet_ntoa(ipHeader[8])  # Source address

        return (rtt, ttl, sequence, saddr)

def sendOnePing(mySocket, destAddr, ID):
    # Header is type (8), code (8), checksum (16), id (16), sequence (16)
    myChecksum = 0
    # Make a dummy header with a 0 checksum.
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    data = struct.pack("d", time.time())
    # Calculate the checksum on the data and the dummy header.
    myChecksum = checksum(header + data)

    # Get the right checksum, and put in the header
    myChecksum = socket.htons(myChecksum)
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    packet = header + data

    mySocket.sendto(packet, (destAddr, 1))  # AF_INET address must be tuple, not str

def doOnePing(destAddr, timeout):
    icmp = socket.getprotobyname("icmp")
    # Create a raw socket
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
    myID = os.getpid() & 0xFFFF  # Return the current process ID
    sendOnePing(mySocket, destAddr, myID)
    delay = receiveOnePing(mySocket, myID, timeout, destAddr)

    mySocket.close()
    return delay

# GUI Code using tkinter
class PingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ping Tool")
        self.root.resizable(0,0)

        # Initialize running_flag as an instance variable
        self.running_flag = [False]  # Use a list to pass the flag reference

        # Initialize statistics variables
        self.packets_sent = 0
        self.packets_received = 0
        self.rtt_min = float('inf')
        self.rtt_max = float('-inf')
        self.rtt_sum = 0

        self.host_label = tk.Label(self.root, text="Enter Host:")
        self.host_label.pack(pady=5)

        self.host_entry = tk.Entry(self.root, width=40)
        self.host_entry.pack(pady=5)

        self.ping_button = tk.Button(self.root, text="Start Ping", command=self.start_ping)
        self.ping_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop Ping", command=self.stop_ping, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.result_text = tk.Text(self.root, height=10, width=70, wrap=tk.WORD)
        self.result_text.pack(pady=0)

    def start_ping(self):
        host = self.host_entry.get()
        if not host:
            messagebox.showerror("Input Error", "Please enter a host.")
            return

        # Add the initial "Pinging ..." message and don't clear it
        self.result_text.delete(1.0, tk.END)  # Clear previous results
        self.result_text.insert(tk.END, f"Pinging {host}...\n")
        
        # Reset statistics before starting
        self.packets_sent = 0
        self.packets_received = 0
        self.rtt_min = float('inf')
        self.rtt_max = float('-inf')
        self.rtt_sum = 0

        self.running_flag[0] = True  # Set the flag to start pinging
        self.ping_thread = threading.Thread(target=self.run_ping, args=(host,))
        self.ping_thread.daemon = True  # Daemonize the thread
        self.ping_thread.start()

        self.ping_button.config(state=tk.DISABLED)  # Disable the Start button
        self.stop_button.config(state=tk.NORMAL)    # Enable the Stop button

    def run_ping(self, host):
        try:
            result = ""
            # Resolve the host to its IP address
            try:
                dest_ip = socket.gethostbyname(host)
            except socket.gaierror:
                messagebox.showerror("Host Resolution Error", f"Unable to resolve host: {host}")
                self.stop_ping()
                return
            
            while self.running_flag[0]:  # Check the flag to stop pinging
                ping_result = doOnePing(dest_ip, 1)
                self.packets_sent += 1
                if ping_result:
                    rtt, ttl, sequence, saddr = ping_result
                    self.packets_received += 1
                    self.rtt_min = min(self.rtt_min, rtt)
                    self.rtt_max = max(self.rtt_max, rtt)
                    self.rtt_sum += rtt
                    result += f"16 bytes from {saddr}: icmp_seq={sequence} ttl={ttl} time={rtt:.3f} ms\n"
                else:
                    result += f"Request timed out.\n"
                self.update_result(result)  # Update the result text box
                time.sleep(1)
            # Show statistics when stopped
            self.show_statistics(result)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            self.ping_button.config(state=tk.NORMAL)  # Re-enable the Start button
            self.stop_button.config(state=tk.DISABLED)  # Disable the Stop button

    def stop_ping(self):
        self.running_flag[0] = False  # Set the flag to stop pinging

    def update_result(self, result):
        """Update the result text box in the main thread."""
        self.result_text.delete(1.0, tk.END)  # Clear previous results
        self.result_text.insert(tk.END, f"Pinging {self.host_entry.get()}...\n")  # Re-insert the "Pinging ..." message
        self.result_text.insert(tk.END, result)  # Append new results
        self.result_text.yview(tk.END)  # Scroll to the end

    def show_statistics(self, result):
        """Show the statistics when pinging is stopped."""
        packet_loss = 100 * (self.packets_sent - self.packets_received) / self.packets_sent
        avg_rtt = self.rtt_sum / self.packets_received if self.packets_received > 0 else 0
        stats = f"\n--- Ping Statistics ---\n" \
                f"Packets Sent = {self.packets_sent}\n" \
                f"Packets Received = {self.packets_received}\n" \
                f"Packet Loss = {packet_loss:.1f}%\n" \
                f"Round-trip min/avg/max = {self.rtt_min:.3f}/{avg_rtt:.3f}/{self.rtt_max:.3f} ms\n"
        self.result_text.insert(tk.END, stats)

if __name__ == "__main__":
    root = tk.Tk()
    app = PingApp(root)
    root.mainloop()
