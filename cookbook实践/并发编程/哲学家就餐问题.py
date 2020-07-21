# “哲学家就餐问题”，作为本节最后一个例 子。
# 题目是这样的：五位哲学家围坐在一张桌子前，
# 每个人面前有一碗饭和一只筷子。
# 在这里每个哲学家可以看做是一个独立的线程，
# 而每只筷子可以看做是一个锁。每个哲 学家可以处在静坐、思考、吃饭三种状态中的一个。
# 需要注意的是，每个哲学家吃饭是 需要两只筷子的，
# 这样问题就来了：如果每个哲学家都拿起自己左边的筷子，
# 那么他们 五个都只能拿着一只筷子坐在那儿，直到饿死。
# 此时他们就进入了死锁状态。下面是一
# 个简单的使用死锁避免机制解决“哲学家就餐问题”的实现：
import threading
import acquire

# The philosopher thread
def philosopher(left, right):
    while True:
        with acquire(left,right):
            print(threading.currentThread(), 'eating')
# The chopsticks (represented by locks)
NSTICKS = 5
chopsticks = [threading.Lock() for n in range(NSTICKS)]
# Create all of the philosophers
for n in range(NSTICKS):
    t = threading.Thread(target=philosopher,
                         args=(chopsticks[n],
                               chopsticks[(n+1) % NSTICKS]))
t.start()

