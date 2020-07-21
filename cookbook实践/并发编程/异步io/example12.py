import asyncio

import time, sys, os
import threading
import concurrent
"""
异步操作中如果处理同步的函数问题
多个协程任务的并行
在事件循环中动态的添加同步函数
解决方案是，先启一个子线程，
这个线程用来跑事件循环loop，
然后动态的将同步函数添加到事件循环中

"""
# 定义阻塞的函数
def ping(url):
    print("阻塞函数开始运行,当前的线程ID为:",threading.current_thread())
    time.sleep(2)
    print("模拟ping 输出 ",url)
    print("阻塞函数运行结束,当前的线程ID为:",threading.current_thread()) 

def start_thread_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

if __name__ == '__main__':
    """
    这里执行器是使用concurrent.futures 下的两个类，
    一个是thread一个是process，也就是执行器可以分为线程执行器和进程执行器。
    它们在初始化的时候都有一个max_workers参数，如果不传则根据系统自身决定。
    """
    print("In main thread", threading.current_thread())
    loop = asyncio.get_event_loop()
    t = threading.Thread(target=start_thread_loop, args=(loop,))
    t.start()
    
    threadingexcutor = concurrent.futures.ThreadPoolExecutor(2)
    processexcutor = concurrent.futures.ProcessPoolExecutor()
    # 在主线程中动态添加同步函数
    
    loop.run_in_executor(processexcutor,ping, "www.baidu.com")
    loop.run_in_executor(processexcutor,ping,"www.qq.com")
    loop.run_in_executor(processexcutor,ping,"www.yangyanxing.com")
    print('主线程不会阻塞')