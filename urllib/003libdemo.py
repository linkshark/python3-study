# urlopen get请求
import urllib.request
# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))
# response=urllib.request.urlopen("http://www.baidu.com")
# print(type(response))
# print(response.read().decode('utf-8'))
# urllib post请求

#代理
proxy_header = urllib.request.proxy_bypass_environment(
    {
        'http':'http://127.0.0.1',
        'https':'https://'

    }

)


