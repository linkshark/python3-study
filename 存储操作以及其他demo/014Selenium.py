from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.common.exceptions import  NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# url = "https://www.zhihu.com/explore"
# headers ={
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }
# browser.get(url)
# logo = browser.find_element_by_id('zu-top-add-question')
# print(logo.text)

# browser = webdriver.Chrome()
# url ="http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# browser.get(url)
# browser.switch_to_frame('iframeResult')
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('No LOGO')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)


#$%^&*(延时等待
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get("https://www.zhihu.com/explore")
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)

#$%^&显式等待
#隐式等待的效果其实并没有那么好，因为我们只是规定了一个固定时间，而页面的加载时间是受到网络条件影响的。
# 所以在这里还有一种更合适的显式等待方法，它指定好要查找的节点，然后指定一个最长等待时间。如果在规定时间内加载出来了这个节点，那就返回查找的节点，如果到了规定时间依然没有加载出该节点，则会抛出超时异常。

# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser, 0.05)
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)

# cookie  操作
browser =  webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
# browser.add_cookie({"name":"shark","age":'18'})
browser.add_cookie({'name': 'shark', 'age': '18', 'value': 'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())




