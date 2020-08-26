import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#发送到的用户的ip和使用的端口
s.bind(('127.0.0.1',8888))
print("绑定UDP到8888端口")
data,addr = s.recvfrom(1024)
data = float(data)*1.8+32
send_data = ('转换后的温度（单位：华摄氏度）：'+str(data))
print('recived from %s:%s.'% addr)
s.sendto(send_data.encode(),addr)
s.close()