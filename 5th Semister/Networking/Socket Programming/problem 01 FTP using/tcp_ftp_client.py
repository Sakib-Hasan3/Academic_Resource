import socket
import time

HOST = '127.0.0.1'
PORT = 5000
CHUNK_SIZE = 100  # 100 bytes

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(3)  # timeout = 3 sec
client.connect((HOST, PORT))

filename = r"E:\Socket Programming\problem 01 FTP using\testfile.txt"

with open(filename, "rb") as f:
    while True:
        chunk = f.read(CHUNK_SIZE)

        if not chunk:
            break  # file finished

        # পুনরায় পাঠানোর জন্য লুপ
        while True:
            try:
                client.sendall(chunk)

                # ACK এর জন্য অপেক্ষা
                ack = client.recv(1024)

                if ack == b"ACK":
                    print("ACK received. Sending next chunk...")
                    break
            except socket.timeout:
                print("Timeout! Resending chunk...")
                continue

# File end signal
client.sendall(b"EOF")

client.close()
