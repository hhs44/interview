import asyncio
import time


async def testa(x):
    print('in test a')
    await asyncio.sleep(3)
    print("runing a")
    return x

async def testb(x):
    print('in test b')
    await asyncio.sleep(1)
    print("runing b")
    return x

async def main():
    start = time.time()
    taska = loop.create_task(testa(1))
    taskb = loop.create_task(testb(2))
    print(testa)
    print(testb)
    print("________________________________________________________________")
    print(taska.done(),taskb.done())
    await taska
    await taskb
    print("________________________________________________________________")
    print(taska.done(),taskb.done())
    print(taska.result(),taskb.result())
    print(f"use {time.time() - start} time")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    