import asyncio

import time, sys, os
import threading
"""
异步操作中如果处理同步的函数问题
多个协程任务的并行, 传统方法
loop.run_forever()
"""
# 定义的阻塞函数
def ping(url):
    print("阻塞函数开始运行")
    time.sleep(2)
    os.system("ping %s"%url)
    print("阻塞函数运行结束")

async def asyncfunc1():
    print("suspending func1")
    await asyncio.sleep(1)
    print("func func1", threading.current_thread())
    print("resuming func1")
    return "func1"


async def asyncfunc2():
    print("suspending func2")
    await asyncio.sleep(1)
    print("func func2", threading.current_thread())
    print("resuming func2")
    return "func2"

# 回调函数
def callbackfunc(task):
    print("task flished rest:", task.result())
    # 协程执行完备结束事件循环
    # loop.stop()
    

async def main():
    task1 = loop.create_task(asyncfunc1())
    task2 = loop.create_task(asyncfunc2())
    # 给task 添加一个回调函数
    task1.add_done_callback(callbackfunc)
    task2.add_done_callback(callbackfunc)
    result = await asyncio.gather(task1, task2)
    print(result)
# 协程中控制任务

# 2、多个协程任务的运行
if __name__ == '__main__':
    print("In main thread", threading.current_thread())
    t1 = threading.Thread8(target=ping,args=("www.baidu.com",))
    t2 = threading.Thread(target=ping,args=("www.yangyanxing.com",))
    t3 = threading.Thread(target=ping,args=("www.qq.com",))
    t1.start()
    t2.start()
    t3.start()
    