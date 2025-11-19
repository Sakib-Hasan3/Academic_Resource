import os
import sys
import struct
import time
import select
import socket

ICMP_ECHO_REQUEST = 8

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
    global rtt_min, rtt_max, rtt_sum, rtt_cnt
    timeLeft = timeout
    while True:
        startedSelect = time.time()
        whatReady = select.select([mySocket], [], [], timeLeft)
        howLongInSelect = (time.time() - startedSelect)
        if whatReady[0] == []:  # Timeout
            return "Request timed out."

        timeReceived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)

        # Fetch the ICMP header from the IP packet
        icmpHeader = struct.unpack('bbHHh', recPacket[20:28])
        type, code, checksum, packetID, sequence = icmpHeader

        if type != 0:
            return f"Expected type=0, but got {type}"
        if code != 0:
            return f"Expected code=0, but got {code}"
        if ID != packetID:
            return f"Expected ID={ID}, but got {packetID}"

        send_time, = struct.unpack('d', recPacket[28:])
        rtt = (timeReceived - send_time) * 1000
        rtt_cnt += 1
        rtt_sum += rtt
        rtt_min = min(rtt_min, rtt)
        rtt_max = max(rtt_max, rtt)

        ipHeader = struct.unpack('!BBHHHBBH4s4s', recPacket[:20])
        ttl = ipHeader[5]
        saddr = socket.inet_ntoa(ipHeader[8])
        length = len(recPacket) - 20

        return f"{length} bytes from {saddr}: icmp_seq={sequence} ttl={ttl} time={rtt:.3f} ms"

        timeLeft -= howLongInSelect
        if timeLeft <= 0:
            return "Request timed out."

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

def ping(host, timeout=1):
    global rtt_min, rtt_max, rtt_sum, rtt_cnt
    rtt_min = float('+inf')
    rtt_max = float('-inf')
    rtt_sum = 0
    rtt_cnt = 0
    cnt = 0
    if host.startswith("http://") or host.startswith("https://"):
        host = host.split("//")[1]
    
    dest = socket.gethostbyname(host)
    print(f"Pinging {dest} using Python:")

    try:
        while True:
            cnt += 1
            print(doOnePing(dest, timeout))
            time.sleep(1)
    except KeyboardInterrupt:
        if cnt != 0:
            print(f"--- {host} ping statistics ---")
            print(f"{cnt} packets transmitted, {rtt_cnt} packets received, {100.0 - rtt_cnt * 100.0 / cnt:.1f}% packet loss")
            if rtt_cnt != 0:
                print(f"round-trip min/avg/max {rtt_min:.3f}/{rtt_sum / rtt_cnt:.3f}/{rtt_max:.3f} ms")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ICMP_Pinger.py <hostname>")
    else:
        ping(sys.argv[1])
