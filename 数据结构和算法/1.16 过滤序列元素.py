# 你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列


mylist = [1, 4, -5, 10, -7, 2, 3, -1]
"""
方法一：
    使用列表推导式（当输入特别大的时候会占用大量的内存）
方法二：
    使用生成器表达式
方法三： 
    复杂处理时,使用filter(func, iter)，filter创建的是一个迭代器
"""
# pos类型是一个生成器
pos = (n for n in mylist if n > 0)
# 使用for循环输出
for x in pos:
    print(x)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)
# Outputs ['1', '2', '-3', '4', '5']
