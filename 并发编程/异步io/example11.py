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
    loop.call_soon_threadsafe()和主线程是跑在同一个线程中的，
    虽然loop.call_soon_threadsafe()没有阻塞主线程的运行，
    但是由于需要跑的函数ping是阻塞式函数，所以调用了三次，
    这三次结果是顺序执行的，并没有实现并发。 
    如果想要实现并发，需要通过run_in_executor 把同步函数在一个执行器里去执行。
    该方法需要传入三个参数，run_in_executor(self, executor, func, *args) 
    第一个是执行器，默认可以传入None，如果传入的是None，将使用默认的执行器，
    一般执行器可以使用线程或者进程执行器。
    """
    print("In main thread", threading.current_thread())
    loop = asyncio.get_event_loop()
    t = threading.Thread(target=start_thread_loop, args=(loop,))
    t.start()
    
    # 在主线程中动态添加同步函数
    
    loop.run_in_executor(None,ping, "www.baidu.com")
    loop.run_in_executor(None,ping,"www.qq.com")
    loop.run_in_executor(None,ping,"www.yangyanxing.com")
    print('主线程不会阻塞')