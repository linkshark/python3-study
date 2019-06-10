#!/user/bin/env python3
import requests
response = requests.get('https://static.zhihu.com/static/revved/img/index/chengxing_logo@2x.65dc76e8.png')
print(response.content)
with open('/var/tmp/shark.png', 'wb') as f:
    f.write(response.content)
    f.close()


