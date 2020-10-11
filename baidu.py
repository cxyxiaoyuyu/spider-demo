import requests

if __name__ == '__main__':
  url = "https://www.baidu.com/s"

  kw = input('请输入要查询的参数: ')

  param = { 'wd': kw }

  # UA 伪装
  headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
  }

  response = requests.get(url=url,params=param,headers=headers)
  
  page_text = response.text

  with open(kw+'.html','w',encoding='utf-8') as fp:
    fp.write(page_text)
  print('保存成功')
