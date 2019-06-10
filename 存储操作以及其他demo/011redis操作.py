from redis import StrictRedis,ConnectionPool

redis = StrictRedis(host='www.linkjb.com' , port=6379 , db=0 )

#redis.set('name', 'Bob')
#print(redis.get('name'))

# 4. Key 操作
# 在这里主要将 Key 的一些判断和操作方法做下总结：
# 方法	作用	参数说明	示例	示例说明	示例结果
# exists(name)	判断一个key是否存在	name: key名	redis.exists('name')	是否存在name这个key	True
# delete(name)	删除一个key	name: key名	redis.delete('name')	删除name这个key	1
# type(name)	判断key类型	name: key名	redis.type('name')	判断name这个key类型	b'string'
# keys(pattern)	获取所有符合规则的key	pattern: 匹配规则	redis.keys('n*')	获取所有以n开头的key	[b'name']
# randomkey()	获取随机的一个key		randomkey()	获取随机的一个key	b'name'
# rename(src, dst)	将key重命名	src: 原key名 dst: 新key名	redis.rename('name', 'nickname')	将name重命名为nickname	True
# dbsize()	获取当前数据库中key的数目		dbsize()	获取当前数据库中key的数目	100
# expire(name, time)	设定key的过期时间，单位秒	name: key名 time: 秒数	redis.expire('name', 2)	将name这key的过期时间设置2秒	True
# ttl(name)	获取key的过期时间，单位秒，-1为永久不过期	name: key名	redis.ttl('name')	获取name这key的过期时间	-1
# move(name, db)	将key移动到其他数据库	name: key名 db: 数据库代号	move('name', 2)	将name移动到2号数据库	True
# flushdb()	删除当前选择数据库中的所有key		flushdb()	删除当前选择数据库中的所有key	True
# flushall()	删除所有数据库中的所有key		flushall()	删除所有数据库中的所有key	True

# print(redis.exists('name'))
# print(redis.delete('name'))
# randomkey = redis.randomkey()
# print(randomkey)
################################你最喜欢的获取过期时间
# print(redis.expire('name',30))
# print(redis.set("name",'hell'))

# 5. String操作
# Redis 中存在最基本的键值对形式存储，用法总结如下：
# 方法	作用	参数说明	示例	示例说明	示例结果
# set(name, value)	给数据库中key为name的string赋予值value	name: key名 value: 值	redis.set('name', 'Bob')	给name这个key的value赋值为Bob	True
# get(name)	返回数据库中key为name的string的value	name: key名	redis.get('name')	返回name这个key的value	b'Bob'
# getset(name, value)	给数据库中key为name的string赋予值value并返回上次的value	name: key名 value: 新值	redis.getset('name', 'Mike')	赋值name为Mike并得到上次的value	b'Bob'
# mget(keys, *args)	返回多个key对应的value	keys: key的列表	redis.mget(['name', 'nickname'])	返回name和nickname的value	[b'Mike', b'Miker']
# setnx(name, value)	如果key不存在才设置value	name: key名	redis.setnx('newname', 'James')	如果newname这key不存在则设置值为James	第一次运行True，第二次False
# setex(name, time, value)	设置可以对应的值为string类型的value，并指定此键值对应的有效期	name: key名 time: 有效期 value: 值	redis.setex('name', 1, 'James')	将name这key的值设为James，有效期1秒	True
# setrange(name, offset, value)	设置指定key的value值的子字符串	name: key名 offset: 偏移量 value: 值	redis.set('name', 'Hello') redis.setrange('name', 6, 'World')	设置name为Hello字符串，并在index为6的位置补World	11，修改后的字符串长度
# mset(mapping)	批量赋值	mapping: 字典	redis.mset({'name1': 'Durant', 'name2': 'James'})	将name1设为Durant，name2设为James	True
# msetnx(mapping)	key均不存在时才批量赋值	mapping: 字典	redis.msetnx({'name3': 'Smith', 'name4': 'Curry'})	在name3和name4均不存在的情况下才设置二者值	True
# incr(name, amount=1)	key为name的value增值操作，默认1，key不存在则被创建并设为amount	name: key名 amount:增长的值	redis.incr('age', 1)	age对应的值增1，若不存在则会创建并设置为1	1，即修改后的值
# decr(name, amount=1)	key为name的value减值操作，默认1，key不存在则被创建并设置为-amount	name: key名 amount:减少的值	redis.decr('age', 1)	age对应的值减1，若不存在则会创建并设置为-1	-1，即修改后的值
# append(key, value)	key为name的string的值附加value	key: key名	redis.append('nickname', 'OK')	向key为nickname的值后追加OK	13，即修改后的字符串长度
# substr(name, start, end=-1)	返回key为name的string的value的子串	name: key名 start: 起始索引 end: 终止索引，默认-1截取到末尾	redis.substr('name', 1, 4)	返回key为name的值的字符串，截取索引为1-4的字符	b'ello'
# getrange(key, start, end)	获取key的value值从start到end的子字符串	key: key名 start: 起始索引 end: 终止索引	redis.getrange('name', 1, 4)	返回key为name的值的字符串，截取索引为1-4的字符	b'ello'
print(redis.get('name'))










