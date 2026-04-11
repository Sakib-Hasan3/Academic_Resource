import socket
import threading
import random
import os
import time

HOST = '127.0.0.1'
PORT = 8000


BASE_PATH = r"E:\Socket Programming\problem 04 streaming client and server"

def handle_client(data, addr, server):
    filename = data.decode()
    file_path = os.path.join(BASE_PATH, filename)
    print(f"Client {addr} requested: {filename}")
    print(f"Looking for file at: {file_path}")

    if os.path.exists(file_path):
        server.sendto(b'OK', addr)
        time.sleep(0.1)

        with open(file_path, 'rb') as f:
            while True:
                chunk_size = random.randint(1000, 2000)
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                server.sendto(chunk, addr)
                print(f"Sent {len(chunk)} bytes to {addr}")
                time.sleep(0.05)

        server.sendto(b'EOF', addr)
        print(f"Streaming complete for {filename}")
    else:
        server.sendto(b'ERROR', addr)
        print(f"File not found: {filename}")

# Main server
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
server.settimeout(1.0)  # allow clean shutdown

print(f"Streaming Server listening on {HOST}:{PORT}")

try:
    while True:
        try:
            data, addr = server.recvfrom(1024)
            threading.Thread(target=handle_client, args=(data, addr, server)).start()
        except socket.timeout:
            continue
except KeyboardInterrupt:
    print("\nServer manually stopped.")
finally:
    server.close()
