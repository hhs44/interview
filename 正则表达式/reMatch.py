import re

def main():
        name = "<body><h1>hsjhus</h1></body>"


        #ret = re.match(r"[a-zA-Z]\w",name)
        ret = re.match(r"<(\w*)><(\w\d)>.*</\2></\1>", name)
        if ret:
            print("邮箱名为：%s 符合要求。匹配的是%s"%(name,ret.group()))
        else:
            print("邮箱名为：%s 不符合要求。。"% name)

name =main()