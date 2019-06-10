# coding=utf-8
from urllib import request,error

try:
    response = request.urlopen("http://www.baidunimasile.com")
except error.HTTPError as e:
    print("小老弟",e.reason,e.code,e.hdrs,sep="/n")
except error.URLError as e:
    print(e.reason,e.code,e.hdrs,sep="/n")
else:
    print("success")

