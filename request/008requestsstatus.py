# coding=utf-8
import requests
response = requests.get("http://www.jianshu.com")
data =[100,200,300,307]
print("fail") if not response.status_code in data else print("Requests Successfully")
print('hahah') if 100 in data else print("nono")
