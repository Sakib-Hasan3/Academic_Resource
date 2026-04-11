import socket
import threading
import time
import os

HOST = '127.0.0.1'
PORT = 6000

# Base folder যেখানে files রাখা আছে
BASE_PATH = r"E:\Socket Programming\problem 02 concurrent file server"

def handle_client(conn, addr):
    print(f"[THREAD] Started for client {addr}")
    
    # Client থেকে filename নেয়া
    filename = conn.recv(1024).decode()
    print(f"[REQUEST] Client {addr} requested: {filename}")
    
    # Full path তৈরি
    file_path = os.path.join(BASE_PATH, filename)

    if os.path.exists(file_path):
        conn.send(b'OK')
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(1000)  # 1KB chunks
                if not data:
                    break
                conn.sendall(data)
                time.sleep(0.1)  # Optional: smooth transfer
        print(f"[DONE] File {filename} sent to {addr}")
    else:
        conn.send(b'ERROR: File not found')
        print(f"[ERROR] File {filename} not found for {addr}")
    
    conn.close()
    print(f"[CLOSED] Connection with {addr} closed")

# Main server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print(f"[LISTENING] Server running on {HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    print(f"[NEW CONNECTION] {addr}")
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
