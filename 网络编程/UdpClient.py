import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

data = input('请输入需要转化的温度：')

s.sendto(data.encode(),('127.0.0.1',8888))
print(s.recv(1024).decode())
s.close()