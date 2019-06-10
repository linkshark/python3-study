# import requests
# response =requests.get('https://weibo.com/');
# print(response.text)
# print("你好")
from selenium import webdriver
driver =webdriver.Chrome()
driver.get('http://www.baidu.com')
print(driver.page_source)