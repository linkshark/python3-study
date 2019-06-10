# coding=utf-8
import requests
import json
response = requests.get("http://httpbin.org/get")
print(type(response.text))
######这个是json字符串
print(response.text)

#下面两个是json对象
print(json.loads(response.text))
print(response.json())
