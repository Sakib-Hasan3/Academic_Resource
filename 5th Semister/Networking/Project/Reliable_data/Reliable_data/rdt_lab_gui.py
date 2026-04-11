import tkinter as tk
from tkinter import ttk, messagebox
import random
import threading
import time
import hashlib

class Packet:
    """Simple data packet with sequence number, checksum, and data"""
    def __init__(self, seq, data):
        self.seq = seq
        self.data = data
        self.checksum = self.generate_checksum()

    def generate_checksum(self):
        return hashlib.md5((str(self.seq) + self.data).encode()).hexdigest()

    def is_corrupted(self):
        return self.checksum != hashlib.md5((str(self.seq) + self.data).encode()).hexdigest()


class RDTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reliable Data Transfer (RDT) Lab")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        # UI Components
        self.setup_ui()

        # Simulation control
        self.stop_flag = False

    def setup_ui(self):
        # --- Top Section: Input ---
        frame_top = ttk.Frame(self.root)
        frame_top.pack(pady=10)

        ttk.Label(frame_top, text="Enter Data to Send:").grid(row=0, column=0, padx=5, pady=5)
        self.data_entry = ttk.Entry(frame_top, width=60)
        self.data_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_top, text="Packet Loss %:").grid(row=1, column=0, padx=5, pady=5)
        self.loss_entry = ttk.Entry(frame_top, width=10)
        self.loss_entry.insert(0, "10")
        self.loss_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(frame_top, text="Corruption %:").grid(row=2, column=0, padx=5, pady=5)
        self.corrupt_entry = ttk.Entry(frame_top, width=10)
        self.corrupt_entry.insert(0, "10")
        self.corrupt_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        self.start_btn = ttk.Button(frame_top, text="Start Transfer", command=self.start_transfer)
        self.start_btn.grid(row=3, column=0, padx=10, pady=10)

        self.stop_btn = ttk.Button(frame_top, text="Stop", command=self.stop_transfer, state=tk.DISABLED)
        self.stop_btn.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # --- Middle Section: Output ---
        frame_output = ttk.Frame(self.root)
        frame_output.pack(pady=10)

        ttk.Label(frame_output, text="Sender Output:").grid(row=0, column=0, padx=10)
        ttk.Label(frame_output, text="Receiver Output:").grid(row=0, column=1, padx=10)

        self.sender_box = tk.Text(frame_output, width=50, height=20, bg="#e8f4ff")
        self.sender_box.grid(row=1, column=0, padx=10, pady=5)

        self.receiver_box = tk.Text(frame_output, width=50, height=20, bg="#e8ffe8")
        self.receiver_box.grid(row=1, column=1, padx=10, pady=5)

        # --- Bottom Section: Status ---
        self.status_label = ttk.Label(self.root, text="Status: Ready", font=("Arial", 11, "bold"))
        self.status_label.pack(pady=10)

    def log_sender(self, msg):
        self.sender_box.insert(tk.END, msg + "\n")
        self.sender_box.see(tk.END)

    def log_receiver(self, msg):
        self.receiver_box.insert(tk.END, msg + "\n")
        self.receiver_box.see(tk.END)

    def unreliable_channel(self, packet):
        """Simulate packet loss, corruption, or delay"""
        # parse probabilities robustly (avoid ValueError if user types non-numeric)
        try:
            loss_prob = int(self.loss_entry.get())
        except Exception:
            loss_prob = 0
        try:
            corrupt_prob = int(self.corrupt_entry.get())
        except Exception:
            corrupt_prob = 0

        # clamp percentages to valid range
        loss_prob = max(0, min(100, loss_prob))
        corrupt_prob = max(0, min(100, corrupt_prob))

        # Packet loss
        if random.randint(1, 100) <= loss_prob:
            self.log_sender(f"Packet {packet.seq} LOST ❌")
            return None

        # Packet corruption
        if random.randint(1, 100) <= corrupt_prob:
            packet.data = "CORRUPTED"
            self.log_sender(f"Packet {packet.seq} CORRUPTED ⚠️")

        # Simulate delay
        time.sleep(random.uniform(0.5, 1.5))
        return packet

    def send_packet(self, packet):
        # Use an iterative retry loop instead of recursion to avoid deep recursion on repeated losses
        max_retries = 5
        attempt = 0
        while not self.stop_flag and attempt <= max_retries:
            self.log_sender(f"Sending Packet {packet.seq} [{packet.data}] ... (Attempt {attempt+1})")
            transmitted = self.unreliable_channel(packet)

            if transmitted is None:
                attempt += 1
                self.log_sender(f"No ACK received for Packet {packet.seq}. RETRANSMITTING... (Retry {attempt})")
                time.sleep(1)
                continue

            # Deliver to receiver
            self.receive_packet(transmitted)
            return

        # If we get here, the packet failed after retries or stop_flag set
        if self.stop_flag:
            self.log_sender(f"Transmission of Packet {packet.seq} interrupted by user.")
        else:
            self.log_sender(f"Packet {packet.seq} failed after {max_retries} retries. Giving up.")

    def receive_packet(self, packet):
        """Receiver side logic"""
        self.log_receiver(f"Received Packet {packet.seq}: [{packet.data}]")
        if packet.data == "CORRUPTED":
            self.log_receiver(f"Packet {packet.seq} is corrupted ❌ (No ACK sent)")
            return

        # Verify checksum
        if packet.is_corrupted():
            self.log_receiver(f"Packet {packet.seq} failed checksum ❌")
            return

        # Send ACK
        self.log_receiver(f"ACK {packet.seq} sent ✅")
        self.status_label.config(text=f"Status: Packet {packet.seq} delivered successfully")

    def transfer_data(self):
        data = self.data_entry.get().strip()
        if not data:
            messagebox.showerror("Error", "Please enter data to send.")
            return

        seq = 1
        for ch in data:
            if self.stop_flag:
                break
            packet = Packet(seq, ch)
            self.send_packet(packet)
            seq += 1
            time.sleep(0.5)

        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Status: Transfer Complete ✅")

    def start_transfer(self):
        self.sender_box.delete(1.0, tk.END)
        self.receiver_box.delete(1.0, tk.END)
        self.stop_flag = False
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        threading.Thread(target=self.transfer_data, daemon=True).start()

    def stop_transfer(self):
        self.stop_flag = True
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Status: Transfer Stopped ⛔")


if __name__ == "__main__":
    root = tk.Tk()
    app = RDTApp(root)
    root.mainloop()
