import requests
from bs4 import BeautifulSoup
import pymysql
from pyquery import PyQuery as pq

# db = pymysql.connect(host = 'www.linkjb.com' ,user = 'root',password = 'xiongge' ,port = 3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print("database version:",data)
# db.close()

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
html = requests.get(url , headers = headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
db = pymysql.connect(host = 'www.linkjb.com',user = 'root',password = 'xiongge',port = 3306,db = 'pachong')
cursor = db.cursor()
sql = 'insert into douban(title,author,text) values(%s,%s,%s)'
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    try:
        # print(question,author,answer)
        cursor.execute(sql,(question,author,answer))
        db.commit()
    except:
        print("error")
        db.rollback()
db.close()


sql = 'select * from douban'
try:
    db = pymysql.connect(host = 'www.linkjb.com',user = 'root',password = 'xiongge',port = 3306,db = 'pachong')
    cursor = db.cursor()
    cursor.execute(sql)
    print("总条数:",cursor.rowcount)
    row = cursor.fetchone()
    a=0
    while row:
        a+=1
        print("Row:",a,row)
        row = cursor.fetchone()
except:
    print("error")


    # file = open('explore.txt', 'a', encoding='utf-8')
    # file.write('\n'.join([question, author, answer]))
    # file.write('\n' + '=' * 100 + '\n')
    # file.close()
    #################简写
    # with open('explore1.txt','a',encoding='utf-8') as file:
    #     file.write('\n'.join([question,author,answer]))
    #     file.write('\n' + '*' * 100 + '\n')