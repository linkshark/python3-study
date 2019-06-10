# coding=utf-8
import requests
from requests.exceptions import ReadTimeout

try:
    response = requests.get("http://httpbin.org/get" ,timeout = 0.5 )
    print(response.status_code)
except ReadTimeout:
    print("Timeout")