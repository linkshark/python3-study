# coding=utf-8
# import json
#
# import requests
# from urllib.parse import urlencode
# from requests.exceptions import RequestException
# from pyquery import PyQuery as pq
# from  bs4 import BeautifulSoup
# import re
# headers = {
# "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
# }
#
# def get_page_index(offset,keyword):
#     data ={
#         'offset':offset,
#         'format': 'json',
#         'keyword': keyword,
#         'autoload': 'true',
#         'count': '20',
#         'cur_tab': 3,
#
#     }
#     url = "https://www.toutiao.com/search_content/?" + urlencode(data)
#     try:
#         response = requests.get(url,headers = headers)
#         if response.status_code == 200:
#             return response.text
#         return None
#     except RequestException:
#         print("请求页面"+url+"失败")
#         return None
# def parse_page_index(html):
#     data = json.loads(html)
#     if data and 'data' in data.keys():
#         for item in data.get('data'):
#             yield item.get('article_url')
#
#
# def get_page_detail(url):
#     try:
#         response = requests.get(url,headers = headers)
#         if response.status_code == 200:
#             return response.text
#         return None
#     except RequestException:
#         print("请求详情页面"+url+"失败")
#         return None
#
# def parse_page_detail(html):
#     soup = BeautifulSoup(html,'lxml')
#     title = soup.select('title')[0].get_text()
#     image_pattern = re.compile('gallery: JSON.parse("(.*?)")',re.S)
#     result = re.search(image_pattern,html)
#     if result:
#         print(result.group(1))
#
#     # items = doc('.article-box').items()
#     # for item in items:
#     #     title = item.find('.article-title')
#     #     print(title)
#
#
#
#
# def main():
#     html = get_page_index(0,"美女")
#     # print(html)
#     for url in parse_page_index(html):
#         html = get_page_detail(url)
#         # if html:
#         #     parse_page_detail(html)
#         print(html)
# if __name__ == '__main__':
#     main()

import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool


# # 在这里我们用 urlencode() 方法构造了请求的 GET 参数，然后用 Requests 请求这个链接，如果返回状态码为 200，则调用 response 的 json() 方法将结果转为 Json 格式，然后返回。
# headers = {
#     'Referer': 'https://m.weibo.cn/u/2145291155',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
#     'X-Requested-With': 'XMLHttpRequest',
# }
# def get_page(offset):
#     params = {
#         'offset': offset,
#         'format': 'json',
#         'keyword': '街拍',
#         'autoload': 'true',
#         'count': '20',
#         'cur_tab': '1',
#     }
#     url = 'http://www.toutiao.com/search_content/?' + urlencode(params)
#     try:
#         response =requests.get(url,headers = headers)
#         if response.status_code == 200:
#             return response.json()
#     except requests.ConnectionError:
#         return None
#
# # 接下来我们再实现一个解析方法，提取每条数据的 image_detail 字段中的每一张图片链接，将图片链接和图片所属的标题一并返回，构造一个生成器，代码如下
# def get_image(json):
#     if json.get('data'):
#         for item in json.get('data'):
#             title = item.get('title')
#             images = item.get('image_list')
#             for image in images:
#                 yield {
#                     'image' : image.get('url'),
#                     'title' :title
#                 }
# # 接下来我们实现一个保存图片的方法，item 就是刚才get_images() 方法返回的一个字典，在方法中我们首先根据 item 的 title 来创建文件夹，然后请求这个图片链接，获取图片的二进制数据，以二进制的形式写入文件，图片的名称可以使用其内容的 MD5 值，这样可以去除重复。
# def save_image(item):
#     if not os.path.exists(item.get('title')):
#         os.mkdir(item.get('title'))
#     try:
#         response = requests.get(item.get('image'))
#         if response.status_code == 200:
#             file_path = '{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
#         if not os.path.exists(file_path):
#             with open(file_path,'wb') as f:
#                 f.write(response.content)
#         else:
#             print('Already Download',file_path)
#     except:
#         print('Failed to Save Image')
# # 最后我们只需要构造一个 offset 数组，遍历 offset，提取图片链接，并将其下载即可。
# def main(offset):
#     json = get_page(offset)
#     for item in get_image(json):
#         print(item)
#         save_image(item)
# GROUP_START = 1
# GROUP_END = 20
#
# if __name__ == '__main__':
#     pool = Pool()
#     groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
#     pool.map(main, groups)
#     pool.close()
#     pool.join()


import requests
from urllib.parse import urlencode
from requests import codes
import os
from hashlib import md5
from multiprocessing.pool import Pool

headers = {
    'Referer': 'https://m.weibo.cn/u/2145291155',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    base_url = 'https://www.toutiao.com/search_content/?'
    url = base_url + urlencode(params)
    try:
        resp = requests.get(url,headers = headers)
        if codes.ok == resp.status_code:
            return resp.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield {
                    'image': 'https:' + image.get('url'),
                    'title': title
                }


def save_image(item):
    img_path = 'img' + os.path.sep + item.get('title')
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    try:
        resp = requests.get(item.get('image'),headers = headers)
        if codes.ok == resp.status_code:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(resp.content).hexdigest(),
                file_suffix='jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                print('Downloaded image path is %s' % file_path)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image，item %s' % item)


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


GROUP_START = 0
GROUP_END = 200

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join




