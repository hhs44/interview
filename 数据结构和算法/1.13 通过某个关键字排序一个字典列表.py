# 你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。

rows = [{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
        ]
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
# 使用lambda表达式
print(rows_by_fname)
print(rows_by_uid)