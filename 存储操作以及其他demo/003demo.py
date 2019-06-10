# char-set = utf-8
import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver

context = requests.get("https://www.douban.com").text
text = context.__str__();
soup = BeautifulSoup(text,'lxml')
brower = webdriver.Chrome()
s= []
qq = 0;
for a in soup.find_all('a'):
    pp = a['href']
    print(pp),
    brower.get(pp)











