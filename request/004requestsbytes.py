# coding=utf-8
import requests
response = requests.get("http://www.linkjb.com/favicon.ico")
#print(type(response.text),type(response.content))
# print(response.text)
# print(response.content)

with open('favicon.ico','wb') as f:
    f.write(response.content)
    f.close()


