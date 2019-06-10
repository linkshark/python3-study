# coding=utf-8
import requests
import re

# content = requests.get("https://book.douban.com/").text
# # content = re.search('<ul class="list-col list-col5 list-express slide-item">.*?</ul>', content, re.S).group()
# # pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
# # results = re.findall(pattern, content)
# # for result in results:
# #     url, name, author, date = result
# #     author = re.sub('\s', '', author)
# #     date = re.sub('\s', '', date)
# #     print(url, name, author, date)
content = requests.get("https://book.douban.com/").text
pattern = re.compile('<div.*?info">.*?more-meta">.*?title">(.*?)</h4>.*?author">(.*?)</span>.*?</div>',re.S)
results = re.findall(pattern,content)
for result in results:
    title,author =result
    title = re.sub("\s","",title)
    title = re.sub("&nbsp", "", title)
    author = re.sub("\s","",author)
    author = re.sub("&nbsp?;?/", "", author)
    print(title.strip(),author.strip())
