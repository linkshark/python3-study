import pymongo
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from urllib.parse import quote
import json

# browser = webdriver.Chrome()
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome()

wait = WebDriverWait(browser, 10)
MAX_PAGE=100
KEYWORD = 'iphonexs max'
client = pymongo.MongoClient('mongodb://www.linkjb.com:27017/')
db = client.taobao
collection = db.iphonexsmax
#
# def search():
#     browser.get('https://www.taobao.com')
#     input = wait.until(
#         EC.presence_of_element_located((By.CSS_SELECTOR,"#q"))
#     )
#     submit = wait.until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_TSearchForm > div.search-button > button"))
#     )
#
#     input.send_keys('美食')
#     submit.click()
#
# def main():
#     search()
#
# if __name__ == '__main__':
#     main()




#$%^&*(错误示范
# def index_page(page):
#     """
#     爬取索引页
#     :param page: 页码
#     :return:
#     """
#     print("正在爬取第",page,'页')
#     try:
#         url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
#         browser.get(url)
#         if page > 1:
#             input = wait.until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form > input'))
#             )
#             submit = wait.until(
#                 EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager  div.form > span.btn.J_Submit'))
#             )
#             input.clear()
#             input.send_keys(page)
#             submit.click()
#         wait.until(
#             EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager  li.item.active > span'),str(page))
#         )
#         wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .items .item')))
#         get_products()
#     except TimeoutException:
#         index_page(page)
#
# def get_products():
#     """
#         提取商品数据
#     """
#     html = browser.page_source
#     doc = pq(html)
#     items = doc('.m-itemlist .items .item').items()
#
#     for item in items:
#         if item != None:
#             product = {
#                 # 'image': "https:"+item.find('.pic img').attr('src')
#                 'image': "https:" + item.find('.pic .img').attr('data-src'),
#                 'price': item.find('.price').text(),
#                 'deal': item.find('.deal-cnt').text(),
#                 'title': item.find('.title').text(),
#                 'shop': item.find('.shop').text(),
#                 'location': item.find('.location').text()
#             }
#             print(product)
#             save_to_mongo(product)
#
#
# def save_to_mongo(result):
#     """
#         保存至MongoDB
#         :param result: 结果
#     """
#     try:
#         # result = json.dumps(result,encoding = 'utf-8')
#         if collection.insert(result):
#             print('存储成功')
#     except Exception:
#         print('存储失败')
#
#
#
#
#
#
#
#
#
#
#
#
# def main():
#     for i in range(1,MAX_PAGE+1):
#         index_page(i)
#     browser.close()
#
#
# if __name__ == '__main__':
#     main()

def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    """
    提取商品数据
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    """
    保存至MongoDB
    :param result: 结果
    """
    try:
        if collection.insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')


def main():
    """
    遍历每一页
    """
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
    browser.close()


if __name__ == '__main__':
    main()






