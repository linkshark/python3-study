# coding=utf-8
# 模式	描述
# \w	匹配字母数字及下划线
# \W	匹配非字母数字及下划线
# \s	匹配任意空白字符，等价于 [\t\n\r\f].
# \S	匹配任意非空字符
# \d	匹配任意数字，等价于 [0-9]
# \D	匹配任意非数字
# \A	匹配字符串开始
# \Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串
# \z	匹配字符串结束
# \G	匹配最后匹配完成的位置
# \n	匹配一个换行符
# \t	匹配一个制表符
# ^	匹配字符串的开头
# $	匹配字符串的末尾
# .	匹配任意字符，除了换行符，当 re.DOTALL 标记被指定时，则可以匹配包括换行符的任意字符
# [...]	用来表示一组字符，单独列出：[amk] 匹配 'a'，'m' 或 'k'
# [^...]	不在 [] 中的字符：abc 匹配除了 a,b,c 之外的字符。
# *	匹配 0 个或多个的表达式。
# +	匹配 1 个或多个的表达式。
# ?	匹配 0 个或 1 个由前面的正则表达式定义的片段，非贪婪方式
# {n}	精确匹配 n 个前面表达式。
# {n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
# `a	b`	匹配 a 或 b
# ( )	匹配括号内的表达式，也表示一个组
# 总结 尽量使用泛匹配,使用括号得到匹配目标,尽量使用非贪婪模式,又换号符就用re.S
import re
content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}.*Demo$',content,flags=0)
# print(result)
# print(result.group())
# print(result.span())
result = re.match("^Hello\s(\d+)\s(\d+)\sWorld.*Demo$",content)
print(result)
print(result.group(1))
print(result.group(2))
print(result)

