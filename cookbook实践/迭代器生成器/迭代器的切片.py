import  itertools

def count(n):
    while True:
        yield n 
        n += 1
     
c = count(0)
   
for x in itertools.islice(c,10,20):
    print(x)
    

# 可迭代对象的忽略操作

# from itertools import dropwhile
# text = "#sssssss\n"
# for line in dropwhile(lambda line:line.startswith("#"),text):
#     print(line, end='')
    
    