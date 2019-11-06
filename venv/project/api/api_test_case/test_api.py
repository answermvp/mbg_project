import requests

r = requests.get('http://httpbin.org/json')
print (r.text)