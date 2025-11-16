import socket
import os

HOST = '127.0.0.1'
PORT = 6000

# Folder যেখানে server files আছে → এখানেই download হবে
SAVE_FOLDER = r"E:\Socket Programming\problem 02 concurrent file server"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

filename = input("Enter filename to download: ")
client.send(filename.encode())

# Server response check
response = client.recv(1024)
if response == b'OK':
    save_name = os.path.join(SAVE_FOLDER, f'downloaded_{filename}')
    with open(save_name, 'wb') as f:
        while True:
            data = client.recv(1000)
            if not data:
                break
            f.write(data)
    print(f"File downloaded successfully as: {save_name}")
else:
    print(response.decode())

client.close()
