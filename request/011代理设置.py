# coding=utf-8
import requests
#8090 1080

#$%^&* 可以去西刺获取代理IP

proxies ={
    # "http" : 'http://183.62.196.10:3128',
    # "https" : 'https://114.113.126.82:80',
    "http" : 'socks5://127.0.0.1:1080',
    "https" : 'socks5://127.0.0.1:1080',
}
headers = {
"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
}

response = requests.get("https://www.taobao.com" , proxies = proxies , headers = headers)

print(response.text)

#$%^$%^& 代理IPAPI http://api.xicidaili.com/free2016.txt

