# 怎样在两个字典中寻寻找相同点（比如相同的键、相同的值等等）？

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}
# 键值有相同点的键
print(b.keys() & a.keys())
# 前者减去后者没有的
print(b.keys() - a.keys())
# item元素
print(b.items() & a.items())
