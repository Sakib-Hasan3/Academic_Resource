import socket

HOST = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server is running... Waiting for connection...")
conn, addr = server.accept()
print("Connected with:", addr)

# নতুন ফাইলে ডেটা লিখবে
with open("received_file.txt", "wb") as f:
    while True:
        data = conn.recv(1024)

        # শেষ signal
        if data == b"EOF":
            print("File transfer complete.")
            break

        f.write(data)

        # ACK পাঠানো
        conn.sendall(b"ACK")

conn.close()
server.close()
