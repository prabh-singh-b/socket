import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1025))
s.listen(5)

while True:
    conn,addr = s.accept()
    print("connection established with {}".format(addr))
    conn.send("Hi Prabh")
    conn.close()