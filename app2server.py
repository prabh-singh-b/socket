import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1025))
s.listen(5)

while True:
    conn,addr = s.accept()
    print("connection established with {}".format(addr))
    msg = conn.recv(1024)
    msg = msg.decode().upper()
    conn.sendall(msg.encode())
    conn.close()