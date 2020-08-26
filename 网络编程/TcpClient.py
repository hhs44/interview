import socket
s = socket.socket()
host = socket.gethostname()
prot = 12345
s.connect((host,prot))
print('已连接')
info = ''
while info != 'byebye':
    send_data = input('请输入发送内容：')
    s.send(send_data.encode())
    if send_data == 'byebye':
        break
    info = s.recv(1024).decode()
    print("接收到的内容："+info)
s.close()