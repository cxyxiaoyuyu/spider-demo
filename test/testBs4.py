# 文档解析
from bs4 import BeautifulSoup

file = open("./test/test.html",'rb') # 读取 二进制
html = file.read()
bs = BeautifulSoup(html,'html.parser')

print(bs.title)
print(bs.a)




