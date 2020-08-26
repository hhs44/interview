import asyncio

import time, sys, os
import threading
import concurrent
"""
异步操作中如果处理同步的函数问题
获取协程的返回结果

"""
# 定义阻塞的函数
def ping(url):
    print("阻塞函数开始运行,当前的线程ID为:",threading.current_thread(),"进程ID为:",os.getpid())
    time.sleep(4)
    print("模拟ping 输出 ",url)
    print("阻塞函数运行结束,当前的线程ID为:",threading.current_thread())
    return url
    
# 定义两个异步函数
async def asyncfunc1():
    print("Suspending func1")
    await asyncio.sleep(1)
    print("func func1 ", threading.current_thread())
    print('Resuming func1')
    return "func1"
    
async def asyncfunc2():
    print("Suspending func2")
    await asyncio.sleep(2)
    print("func func2 ", threading.current_thread())
    print('Resuming func2')
    return "func2"
    

#定义一个跑事件循环的线程函数    
def start_thread_loop(loop):
    print("loop线程 id 为",threading.current_thread())
    asyncio.set_event_loop(loop)
    loop.run_forever()
    
# 定义一个回调函数
def callbackfunc(task):
    print("task 运行结束,它的结果是:",task.result())
    # loop.stop()
    
async def main():
    t1 = time.time()
    # 使用loop.create_task创建task对象,返回asyncio.tasks.Task对象
    task1 = loop.create_task(asyncfunc1())
    task2 = loop.create_task(asyncfunc2())
    # 使用asyncio.run_coroutine_threadsafe 返回的是concurrent.futures._base.Future对象
    # 注意这个对象没有__await__方法，所以不能对其使用await 但是可以给它添加回调add_done_callback
    task3 = asyncio.run_coroutine_threadsafe(asyncfunc1(),loop)
    task4 = asyncio.run_coroutine_threadsafe(asyncfunc2(),loop)
    
    # 使用loop.run_in_executor创建阻塞的任务，返回asyncio.futures.Future对象
    task5 = loop.run_in_executor(None,ping,"www.baidu.com")
    task6 = loop.run_in_executor(None,ping,"www.yangyanxing.com")
    
    # 使用asyncio.ensure_future()创建任务对象
    task7 = asyncio.ensure_future(asyncfunc1())
    task8 = asyncio.ensure_future(asyncfunc2())
    
    
    task1.add_done_callback(callbackfunc)    
    task2.add_done_callback(callbackfunc)    
    task3.add_done_callback(callbackfunc)
    task4.add_done_callback(callbackfunc)
    task5.add_done_callback(callbackfunc)
    task6.add_done_callback(callbackfunc)
    task7.add_done_callback(callbackfunc)
    task8.add_done_callback(callbackfunc)
   
    result = await asyncio.gather(task1,task2,task5,task6,task7,task8)    
    print(result)
    t2 = time.time()
    print("一共用了%s时间"%(t2-t1))
    
async def mian2():
    result = await asyncio.gather(asyncfunc1(),asyncfunc2(),)
    print(result)
    
def shutdown(loop):
    loop.stop()
    
if __name__=="__main__":
    print("In main thread ",threading.current_thread())
    loop = asyncio.get_event_loop()
    loop2 = asyncio.new_event_loop()
    # 在子线程中运行事件循环,让它run_forever
    t = threading.Thread(target= start_thread_loop, args=(loop,))
    t.start()
    asyncio.run_coroutine_threadsafe(main(),loop)
    print('主线程不会阻塞')