# coding=utf-8
import requests
# response = requests.get('https://httpbin.org/get?name=九堡吴彦祖&age=1314')
# print(response.text)

data = {
    'name' : '九堡吴彦祖',
    'age'  :  18
}
response = requests.get('https://httpbin.org/get',params=data)
print(response.text)