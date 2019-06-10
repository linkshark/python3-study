# coding=utf-8
import http.cookiejar,urllib.request

##########获取网页上的COOKIE
# cookie= http.cookiejar.CookieJar()
# header=urllib.request.HTTPCookieProcessor(cookie)
# opener=urllib.request.build_opener(header)
# response=opener.open("http://www.baidu.com")
# # print(cookie)
# for item in cookie:
#     print(item.name + "=" + item.value)


###########获取网页上的COOKIE并保存到本地
# filename='cookiejar1.txt'
# cookie= http.cookiejar.LWPCookieJar(filename)
# header=urllib.request.HTTPCookieProcessor(cookie)
# opener=urllib.request.build_opener(header)
# response=opener.open("http://www.baidu.com")
# cookie.save(ignore_discard=True,ignore_expires=True)
# # print(cookie)
# for item in cookie:
#     print(item.name + "=" + item.value)

##############将网页上的COOKID带到下一次请求中

cookie=http.cookiejar.LWPCookieJar()
cookie.load('cookiejar1.txt',ignore_expires=True,ignore_discard=True)
headler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(headler)
response=opener.open("http://www.baidu.com")
print(response.read().decode('utf-8'))
