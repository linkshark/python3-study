import csv

#with open('data.csv', 'w') as csvfile:
#######如果想追加写入可以修改为
# with open('data.csv', 'a',encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile, delimiter=' ')
    # writer.writerow(['id', 'name', 'age'])
    # writer.writerow(['10001', 'Mike', 20])
    # writer.writerow(['10002', 'Bob', 22])
    # writer.writerow(['10003', 'Jordan', 21])


    #writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])


    ########字典化数据
    # fieldnames = ['id','name','age']
    # writer = csv.DictWriter(csvfile,fieldnames = fieldnames , delimiter = ' ')
    # writer.writeheader();
    # writer.writerow({'id': '10001' , 'age': 20,'name': '吴彦祖'})
    # writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    # writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})

###############下面开始读取
with open("data.csv","r",encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
