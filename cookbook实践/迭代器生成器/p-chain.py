from itertools import chain


# 实现多个集合的迭代
a = [1,2,3,4]
b = ['x','y','z']

for x in chain(a, b):
    print(x)
    
