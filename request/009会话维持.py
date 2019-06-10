# coding=utf-8

import requests
##########模拟登陆,这是在两个浏览器,所以没有维护
# requests.get("http://httpbin.org/cookies/set/number/1234567890")
# response = requests.get("http://httpbin.org/cookies")
# print(response.text)

####%^&** 现在设置session
s = requests.session()
s.get("http://httpbin.org/cookies/set/number/1234567890")
response = s.get("http://httpbin.org/cookies")
print(response.text)