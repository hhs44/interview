import time
from  threading import Thread

# def process():
#     for i in range(3):
#         time.sleep(1)
#         print("thread name is %s"% threading.current_thread().name)


# class SubThread(threading.Thread):
#     def run(self):
#         for i in range(3):
#             time.sleep(1)
#             msg = "子线程"+self.name+"执行，i="+str(i)
#             print(msg)
def plus():
    print("子线程1开始")
    global g_num
    g_num += 50
    print('g_num is %d ' % g_num)
    print('子线程1结束')


def minus():
    time.sleep(1)
    print('子线程2开始')
    global g_num
    g_num -= 50
    print('g_num is %d '%g_num)
    print('子线程2结束')

g_num =100
if __name__ == '__main__':
    print("---主线程开始----")
    # threds = [threading.Thread(target=process) for i in range(4)]
    # for t in threds:
    #     t.start()
    # for t in threds:
    #     t.join()
    # t1 = SubThread()
    # t2 = SubThread()
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    t1 = Thread(target=plus)
    t2 = Thread(target=minus)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("主线程结束")