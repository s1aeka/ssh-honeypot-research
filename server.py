import socket
from datetime import datetime

HOST = "127.0.0.1"
PORT = 2222
LOG_FILE = "connections.log"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print("Listening on", HOST, PORT)

while True:
    conn, addr = server.accept()
    ip, port = addr

    conn.sendall(b"login: ")
    username = conn.recv(1024).decode().strip()
    conn.sendall(b"Password: ")
    password = conn.recv(1024).decode().strip()
    conn.sendall(b"Login incorrect\n")
    conn.close()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} {ip}:{port} user={username} password={password}\n")
    print("Logged attempt from", ip, "user:", username)