import asyncio
import time

"""
asyncio.wait()的实现
return_whend的配置：
done,pending = await asyncio.wait([testa(1),testb(2)],return_when=asyncio.tasks.FIRST_EXCEPTION)
"""
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
    done, pending = await asyncio.wait([testa(1), testb(2)])
    print(list(done))
    print(list(pending))
    print(list(done)[0].result())
    print(f"use {time.time() - start} time")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    