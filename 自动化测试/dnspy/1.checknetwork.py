import dns.resolver
import os

from eventlet.green import httplib

iplist = []
appdomian = "qq.com"  # 域名前不能加www


# 抓取所有ip列表
def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain, 'A')  # 查询A记录
    except Exception as e:
        print(e)
        return None
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return iplist


# print(get_iplist(appdomian))

def checkip(ip):
    checkurl = ip + ":80"
    getcontent = ""
    httplib.socket.setdefaulttimeout(5)  # 超时
    conn = httplib.HTTPConnection(checkurl)
    try:
        conn.request("GET", "/", headers={"host": appdomian})
        result = conn.getresponse()
        getcontent = result.read().decode("utf-8")
    finally:
        if getcontent.find("html") != -1:
            print("ipOK", checkurl)
        else:
            print("ipNO", checkurl)


iplist = get_iplist(appdomian)
if iplist != None and len(iplist) != 0:
    for ip in iplist:
        checkip(ip)
