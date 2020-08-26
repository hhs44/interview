xpts = [1,5,4]
ypts = [102,32,43]

for x, y in zip(xpts, ypts):
    print(x, y)
    
    
# ---------
from itertools import zip_longest

a = ['x','y','z']
b = [1,2]

for i in zip_longest(a,b):
    print()

print(dict(zip_longest(a,b)))