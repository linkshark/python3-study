# coding=utf-8
from urllib.parse import urlencode
from selenium import webdriver

params = {
    'name' : '这是一条来自python的数据',
    'age'  :  '18'
}
base_url = 'localhost:8080/linkjb/mvc/first?'
url = base_url + urlencode(params)
driver=webdriver.Chrome()
while True:

    driver.get(url)




