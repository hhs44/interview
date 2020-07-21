import asyncio

import time, sys, os
import threading
import concurrent
"""
异步操作中如果处理同步的函数问题
在事件循环中动态的添加异步函数

"""
# 定义两个异步函数
async def asyncfunc1():
    print("Suspending func1")
    await asyncio.sleep(1)
    print("func func1 ", threading.current_thread())
    print('Resuming func1')
    return "func1"
    
async def asyncfunc2():
    print("Suspending func2")
    await asyncio.sleep(1)
    print("func func2 ", threading.current_thread())
    print('Resuming func2')
    return "func2"

#定义一个跑事件循环的线程函数 
def start_thread_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

if __name__ == '__main__':
    """
    在事件循环中动态的添加异步函数
    通过asyncio.run_coroutine_threadsafe在loop上绑定了四个协程函数，
    得到的输出结果为
    主线程不会被阻塞，起的四个协程函数几乎同时返回的结果，
    但是注意，协程所在的线程和主线程不是同一个线程，因为此时事件循环loop是放到了另外的子线程中跑的，
    所以此时这四个协程放到事件循环的线程中运行的
    """
    print("In main thread ",threading.current_thread())
    loop = asyncio.get_event_loop()
    # 在子线程中运行事件循环,让它run_forever
    t = threading.Thread(target= start_thread_loop, args=(loop,))
    t.start()
    asyncio.run_coroutine_threadsafe(asyncfunc1(),loop)
    asyncio.run_coroutine_threadsafe(asyncfunc1(),loop)
    asyncio.run_coroutine_threadsafe(asyncfunc2(),loop)
    asyncio.run_coroutine_threadsafe(asyncfunc2(),loop)
    
    print('主线程不会阻塞')