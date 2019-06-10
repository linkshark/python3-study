# coding=utf-8
import requests

data = {
    "name" : "shark",
    "age"  :  18
}
headers = {
"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"

}
response = requests.post("http://localhost:8080/linkjb/mvc/first",data = data ,headers = headers)
print(response.text)