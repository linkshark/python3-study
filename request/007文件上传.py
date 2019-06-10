# coding=utf-8
import requests
###文件上传
# files ={"file" : open("favicon.ico",'rb')}
# response = requests.post("http://httpbin.org/post",files = files)
# print(response.text)
response = requests.get("http://www.zhihu.com")
print(response.cookies)
for key,value in response.cookies.items():
    print(key + "=" + value)