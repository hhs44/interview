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
    resa, resb = await asyncio.gather(testa(1), testb(2))
    print(f"test a result is {resa}")
    print(f"test b result is {resb}")
    print(f"use {time.time() - start} time")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    