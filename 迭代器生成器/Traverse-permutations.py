from itertools import permutations
from itertools import combinations

items = [1,23,4,5]


# 关系顺序
for p in permutations(items, 4):
    print(p)
    
    # 不关心顺序
    """[summary]:
    函数 itertools. combinations_with_replacement()
     允许同一个元素被选择多次
    """   
for x in combinations(items, 3):
    print(x)
