import socket
import os

HOST = '127.0.0.1'
PORT = 8000
SAVE_PATH = r"E:\Socket Programming\problem 04 streaming client and server"

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(3)

filename = input("Enter filename to download: ")
client.sendto(filename.encode(), (HOST, PORT))

try:
    response, _ = client.recvfrom(1024)
    if response == b'OK':
        save_file = os.path.join(SAVE_PATH, f"downloaded_{filename}")
        with open(save_file, 'wb') as f:
            while True:
                try:
                    data, _ = client.recvfrom(2048)
                    if data == b'EOF':
                        break
                    f.write(data)
                    print(f"Received {len(data)} bytes")
                except socket.timeout:
                    continue
        print(f"File saved as: {save_file}")
    else:
        print("File not found on server.")
except socket.timeout:
    print("Server did not respond.")
finally:
    client.close()
