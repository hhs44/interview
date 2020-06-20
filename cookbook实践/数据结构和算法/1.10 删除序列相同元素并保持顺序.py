# 怎样在一个序列上面保持元素顺序的同时消除重复的值？

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
b = dedupe(a)
print(next(b))

print(b.__next__())
print(b.__next__())
print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())

print(list(dedupe(a)))
"""
改进 笑处元素不可哈希的序列
"""


def dedupe_new(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
list(dedupe_new(a, key=lambda d: (d['x'], d['y'])))
