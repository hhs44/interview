import heapq

a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]

for item in heapq.merge(a, b):
    print(item)
