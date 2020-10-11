import requests  # 模拟浏览器发请求

# 指定url
# 发起请求
# 获取响应数据
# 持久化存储

def main():
  url = 'https://www.sogou.com/'
  response = requests.get(url=url)
  page_text = response.text

  with open('./sougou.html','w') as fp:
    fp.write(page_text)

  print('爬取数据结束')

if __name__ == "__main__":
  main()

