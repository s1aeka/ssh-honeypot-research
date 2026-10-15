import socket

with socket.create_connection(("127.0.0.1", 2222)) as s:
    data = s.recv(1024)
    print("Server says:", data.decode())