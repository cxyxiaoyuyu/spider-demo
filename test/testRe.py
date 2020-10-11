# 正则表达式 字符串模式
import re

# pat = re.compile('AA')
# print(pat.search('CAAAA'))  #search方法 进行查找比对

# m = re.search('asd','Aasd')
# print(m)

# m = re.findall('[a-z]+','abAcaCda')   # 规则 校验字符串
# print(m)

print(re.sub('a','A','abcdcasd'))  # 找到a 替换成A 
