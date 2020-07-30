

class WordCount():
    
    def __init__(self,filename):
        self.filename = filename
        self.wordCount = {}
        self.lines = ""
        self.wordlsit = []
        
    def get_lines(self):
        with open(self.filename) as f:
            self.lines = f.read()

    def get_wordCount(self):
        self.get_lines()
        temp = ""
        t = 0
        for i in self.lines:
            if t == 0 and i.isalpha():
                temp += i  
            elif t == 1 and i.isalpha():
                self.wordlsit.append(temp)
                temp = i
                t = 0
            elif i.isalnum() :
                temp += i
            else:
                t = 1
        self.wordlsit.sort(key=lambda x :x.lower())
        from collections import Counter
        self.wordCount = Counter(self.wordlsit)
        print(self.wordCount)

                
if __name__ == "__main__":
    wordcount = WordCount('Python编程题数据文件.txt')
    wordcount.get_wordCount()