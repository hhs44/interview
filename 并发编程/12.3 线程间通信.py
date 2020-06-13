# 问题
# 你的程序中有多个线程，你需要在这些线程之间安全地交换信息或数据
#
# 解决方案
# 从一个线程向另一个线程发送数据最安全的方式可能就是使用 queue 库中的队列了。
# 创建一个被多个线程共享的 Queue 对象，这些线程通过使用 put() 和 get() 操作来向队列中添加或者删除元素。
# 例如：

from queue import Queue
from threading import Thread


# A thread that produces data
def producer(out_q):
    while True:
        # Produce some data
        data = [1, 2, 3, 4]
        out_q.put(data)


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        # Process the data
        print(data)


# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()


# 案例二：创建一个线程安全的优先级队列

import heapq
import threading

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._count = 0
        self._cv = threading.Condition()
    def put(self, item, priority):
        with self._cv:
            heapq.heappush(self._queue, (-priority, self._count, item))
            self._count += 1
            self._cv.notify()

    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()
            return heapq.heappop(self._queue)[-1]