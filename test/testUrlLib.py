import urllib.request
import urllib.parse

# get 请求访问一个网址
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))  # 对获取到的网页进行utf-8的解码

# post请求 
# data = bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read().decode('utf-8'))

# get 超时处理
'''
try:
  response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.01)
  print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
  print('time out')
'''

# response = urllib.request.urlopen('http://httpbin.org/get')
# print(response.getheader('Server'))
# print(response.getheaders())

# 不让别人发现是爬虫 
# url = 'http://httpbin.org/post'
# url = 'https://www.douban.com'
# data = bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
# headers = { 
#   "Accept": "application/json",
#   "Accept-Encoding": "gzip, deflate",
#   "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
#   "Content-Length": "0",
#   "Host": "httpbin.org",
#   "Origin": "http://httpbin.org",
#   "Referer": "http://httpbin.org/",
#   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
#   "X-Amzn-Trace-Id": "Root=1-5f81e6bb-3792ac0e47329e7817e9c11d"
# }
# req = urllib.request.Request(url=url,headers=headers,data=data,method='POST')
# res = urllib.request.urlopen(req)
# print(res.read().decode('utf-8'))

url = 'https://www.douban.com'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
}
req = urllib.request.Request(url=url,headers=headers)
res = urllib.request.urlopen(req)
print(res.read().decode('utf-8'))