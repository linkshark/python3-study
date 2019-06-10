# coding=utf-8
import requests
headers = {
"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"

}
response = requests.get("https://www.zhihu.com" , headers = headers)
print(response.text)