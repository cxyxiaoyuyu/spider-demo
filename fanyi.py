import requests 
import json

if __name__ == "__main__":
  url = 'https://fanyi.baidu.com/sug'

  headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
  }

  kw = input('请输入要翻译的单词: ')
  data = { 'kw': kw }

  response = requests.post(url=url,data=data,headers=headers)
  # 确认响应数据是json类型的 才可以用json()方法
  dict_obj = response.json()

  # 存储
  fp = open(kw+'.json','w',encoding='utf-8')
  json.dump(dict_obj,fp=fp,ensure_ascii=False)  # 中文不可以使用ascii编码

  print('over!!!')
