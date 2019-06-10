# coding=utf-8
import requests

response =requests.get("https://www.12306.cn",verify=False)
print(response.text)