import time




class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0
    def add(self, name):
        self.names.append(name)
        pass
    def __iter__(self):
        return self

# class ClassIterator(object):
#     def __init__(self,obj):
#         self.obj = obj
#         self.current_num = 0
#
#     def __iter__(self):
#         pass
    def __next__(self):
        if self.current_num<len(self.names):
            ret = self.names[self.current_num]
            self.current_num +=1
            return ret
        else:
            raise StopIteration
classmate = Classmate()
classmate.add("王万")
classmate.add("王玉")
classmate.add("王道")

for trmp in classmate:
    print(trmp)
    time.sleep(1)


