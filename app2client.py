import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1025))
msg = "hi prabh"
s.sendall(msg.encode())
msg = s.recv(1024)
print(msg.decode())
s.close()