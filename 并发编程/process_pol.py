from multiprocessing import Pool
import os, time


def task(name):
    print('子进程（%s）执行task %s。。。' % (os.getpid(), name))
    time.sleep(2)


if __name__ == '__main__':
    print("父进程（%s）" % os.getpid())
    p = Pool(5)
    for i in range(20):
        p.apply_async(task, args=(i,))
    print('等待所有子进程结束')
    p.close()
    p.join()
    print('所有子进程结束')
