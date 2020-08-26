# 你想构造一个字典，它是另外一个字典的子集。

prices = {'ACME': 45.23, 'AAPL': 612.78,
          'IBM': 205.55, 'HPQ': 37.20,
          'FB': 10.75
          }

"""
方法一：字典推导式
通过创建一个元组序列然后把它传给 dict() 函 数也能实现。比如：
p1 = dict((key, value) for key, value in prices.items() if value > 200)
"""
# Make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}
# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
