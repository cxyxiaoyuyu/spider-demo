# 文档解析
from bs4 import BeautifulSoup
import requests
# 标签定位
# 提取标签 标签属性中存储的数据值

# 1 实例化BeautifulSoup对象 将页面源码数据加载到该对象中
#  a 将本地html文档中加到载到该对象中
#  b 将互联网上的html文档加载到对象中
# 2 通过调用BeautifulSoup对象中相关的属性或方法进行标签定位和数据提取
# pip install bs4   pip install lxml


# 解析本地html
html = open("./test/test.html",'rb') # 读取 <_io.BufferedReader name='./test.html'>
bs = BeautifulSoup(html,'html.parser')  # 参数2 也可以是lxml

# 1 bs.tagName
title = bs.title  # <class 'bs4.element.Tag'>  
a = bs.a
# 获取标签文本数据 属性值  text  get_text  attrs
a.text
a.get_text
a.string
a['class']  # 'mnav'

# 2 bs.find(tagName,attrs)
bs.find('div')  # 等同于 bs.div   
bs.find('div',class_="head_wrapper")
bs.find_all('a')  # 返回一个列表

# 3 bs.select(css选择器)
bs.select('.mnav')  # 返回一个列表
bs.select('#wrapper  #u1')

u1 = bs.select('#u1')[0]
u1.text      # '\n新闻\nhao123\n地图\n视频\n贴吧\n更多产品\n'
u1.get_text  # '\n新闻\nhao123\n地图\n视频\n贴吧\n更多产品\n'
u1.string    # None 只可以获取该标签直系文本
# 获取属性值







# 解析互联网上的html
# url = "https://www.baidu.com/s"
# param = { 'wd': 'python' }
# headers = {
#   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
# }
# response = requests.get(url=url,params=param,headers=headers)
# page_text = response.text      # str类型
# bs = BeautifulSoup(page_text,'html.parser')

