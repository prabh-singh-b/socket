import socket
import pickle
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1025))
msg = s.recv(1024)
msg = msg.decode('utf-8')
msg = eval(msg)
msg[0](msg[1])
s.close()