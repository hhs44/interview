import time
import threading

n =100

def plus():
    print("开始抢票")
    global n
    mutex.acquire()
    temp = n
    time.sleep(1)
    n = temp -1
    print('购买成功，还剩%d票 ' % n)
    mutex.release()




if __name__ == '__main__':
    mutex = threading.Lock()
    t_l = []
    print("---主线程开始----")

    for i in range(10):
        t =threading.Thread(target=plus)
        t_l.append(t)
        t.start()
        for t in t_l:
            t.join()

    print("主线程结束")