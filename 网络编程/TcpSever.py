import socket


#创建socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#目的信息
host = socket.gethostname()
port = 12345

#创建服务器
s.bind((host,port))

#设置最大连接数，被动接受TCP客户端连接
s.listen(2)
sock,addr = s.accept()
print('连接已近连接')
info = sock.recv(1024).decode()
#判断是否退出
while info!='byebye':
    if info!='byebye':
        print('接收到的内容：'+info)
    send_data = input('输入内容')
    sock.send(send_data.encode())
    if send_data == 'byebye':
        break
    info = sock.recv(1024).decode()
sock.close()
s.close()

