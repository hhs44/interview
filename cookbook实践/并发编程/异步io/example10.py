import asyncio

import time, sys, os
import threading
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
    print("In main thread", threading.current_thread())
    loop = asyncio.get_event_loop()
    t = threading.Thread(target=start_thread_loop, args=(loop,))
    t.start()
    
    # 在主线程中动态添加同步函数
    loop.call_soon_threadsafe(ping, "www.baidu.com")
    loop.call_soon_threadsafe(ping,"www.qq.com")
    loop.call_soon_threadsafe(ping,"www.yangyanxing.com")
    print('主线程不会阻塞')