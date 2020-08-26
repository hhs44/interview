import time
def countdown(n):
    while n > 0:
        print('T-minus',n)
        n -= 1
        time.sleep(2)

from threading import Thread

t = Thread(target=countdown,args=(10, 0))
t.start()


