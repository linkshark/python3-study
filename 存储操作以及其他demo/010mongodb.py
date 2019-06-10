import pymongo
client = pymongo.MongoClient('mongodb://www.linkjb.com:27017/')
db = client.test
collection = db.students
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
#result = collection.insert([student1,student2])
#print(result)

#results = collection.find({'age': 20})
#########查询大于20的数据
# $lt	小于	{'age': {'$lt': 20}}
# $gt	大于	{'age': {'$gt': 20}}
# $lte	小于等于	{'age': {'$lte': 20}}
# $gte	大于等于	{'age': {'$gte': 20}}
# $ne	不等于	{'age': {'$ne': 20}}
# $in	在范围内	{'age': {'$in': [20, 23]}}
# $nin	不在范围内	{'age': {'$nin': [20, 23]}}
#results = collection.find({'age' : {'$gt' : 20 }})
# for result in results:
#     print(result)


# $regex	匹配正则	{'name': {'$regex': '^M.*'}}	name 以 M开头
# $exists	属性是否存在	{'name': {'$exists': True}}	name 属性存在
# $type	类型判断	{'age': {'$type': 'int'}}	age 的类型为 int
# $mod	数字模操作	{'age': {'$mod': [5, 0]}}	年龄模 5 余 0
# $text	文本查询	{'$text': {'$search': 'Mike'}}	text 类型的属性中包含 Mike 字符串
# $where	高级条件查询	{'$where': 'obj.fans_count == obj.follows_count'}	自身粉丝数等于关注数
# results = collection.find({'name':{'$regex':'^M.*'}})
# for result in results:
#     print(result)

# count = collection.find().count()
# print(count)
#
# ##高级查询
# count = collection.find({'age':{'$gt' : 20}}).count()
# print(count)

#@#$%^&@@@@@@@@@@@@@@@@@@@@@@@@排序
# results = collection.find().sort('name',pymongo.ASCENDING)
# print([result['name'] for result in results])
#                       偏移排序!!!!!!!
# results = collection.find().sort('name',pymongo.ASCENDING).skip(2)
# print([result['name'] for result in results])

#$%^&*(              更新操作
condition = {'name' : 'Mike'}
student = collection.find_one(condition)
student['age'] = 333
result = collection.update(condition,student)
print(result)

