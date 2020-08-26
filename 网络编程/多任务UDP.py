import socket
import  threading


def recv_msg(s):
    # 接收数据
    while True:
        data, addr = s.recvfrom(1024)
        data = float(data)*1.8+32
        print(data)
        print('转换后的温度（单位：华摄氏度）：'+str(data))
        print('recived from %s:%s.'% addr)
def send_msg(s):
    # 发送数据
    while True:
        data = input('请输入需要转化的温度：')
        s.sendto(data.encode(), ('127.0.0.1', 8888))
        print(s.recv(1024).decode())

def main():
    #创建套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 发送到的用户的ip和使用的端口
    s.bind(('127.0.0.1', 8888))
    print("绑定UDP到8888端口")
    t_recv = threading.Thread(target=recv_msg,args=(s,))
    t_send = threading.Thread(target=send_msg, args=(s,))

    t_recv.start()
    t_send.start()
    t_send.join()
    t_recv.join()

if __name__ == '__main__':
    main()