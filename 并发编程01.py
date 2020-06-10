import time
from threading import Thread



# class CountdownTask:
#     def __init__(self):
#         self._running = True
#
#     def terminate(self):
#         self._running = False
#
#     def run(self, n):
#         while self._running and n > 0:
#             print('T-minus', n)
#             n -= 1
#             time.sleep(5)
#
#
# c = CountdownTask()
# t = Thread(target=c.run, args=(10,))
# t.start()
# c.terminate()
# t.join()

class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n
    def run(self):
        while self.n > 0:

            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

c = CountdownThread(5)
c.start()