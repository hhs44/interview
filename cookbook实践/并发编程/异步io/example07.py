import asyncio

import time, sys
import threading
"""
异步操作中如果处理同步的函数问题
loop.run_forever()
"""
def ping(url):
    print("start ping")
    time.sleep(2)

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
    loop.stop()
# 协程中控制任务

# 1、单个协程任务的运行
if __name__ == '__main__':
    print("In main thread", threading.current_thread())
    loop = asyncio.get_event_loop()
    task = loop.create_task(asyncfunc1())
    # 给task 添加一个回调函数
    task.add_done_callback(callbackfunc)
    loop.run_forever()
    print("task result is", task.result())
    
    