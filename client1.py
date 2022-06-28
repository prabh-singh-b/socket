import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1025))
msg = s.recv()
print(msg)
s.close()