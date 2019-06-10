# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains

# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
# #     browser.close()


# browser = webdriver.Chrome()
# try:
#     browser.get("https://www.taobao.com")
#     input_first = browser.find_element_by_id('q')
#     input_second = browser.find_element_by_css_selector('#q')
#     input_third = browser.find_element_by_xpath('//*[@id="q"]')
#     input_forth = browser.find_element(By.ID, 'q')
#     print(input_first,input_second,input_third,input_third)
# finally:
#     browser.close()

# browser = webdriver.Chrome()
# browser.get("https://www.taobao.com")
# lis =browser.find_elements_by_css_selector('.service-bd li')
# for li in lis:
#     print(li)
# browser.close()

# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input = browser.find_element_by_id('q')
# input.send_keys('iphone')
# time.sleep(1)
# input.clear()
# input.send_keys('ipad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()


#$%ˆˆ*()动作链
# 拖拽


# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

#调用原生javascrip
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')


# 获取节点信息
browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))







