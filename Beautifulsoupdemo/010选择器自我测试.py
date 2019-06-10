# coding=utf-8
import requests
from bs4 import BeautifulSoup
headers = {
"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"

}
response = requests.get("https://www.douban.com",headers = headers).text
text = response.__str__();
soup = BeautifulSoup(text,'lxml')
#print(soup)
a = []
for li in soup.select('a') :
    # if li.attrs['href'].
    # a.append()
    print(type(li.__getattr__('href')))
