# coding=utf-8
import  re
content = 'price is $5.00'
result = re.match('price is \$5\.00',content)
print(result)