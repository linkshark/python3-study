# coding=utf-8
from bs4 import BeautifulSoup
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
soup = BeautifulSoup(html,'lxml')
# print(soup.p.contents)
# print(soup.children)#这是一个迭代器类型
# #所有子节点
# for i,child in enumerate(soup.p.children):
#     print(i,child)
for i,child in enumerate(soup.p.descendants):
    print(i,child)
