import socket

with socket.create_connection(("127.0.0.1", 2222)) as s:
    print(s.recv(1024).decode(), end="")
    s.sendall(b"dani\n")
    print(s.recv(1024).decode(), end="")
    s.sendall(b"lololol\n")
    print(s.recv(1024).decode(), end="")