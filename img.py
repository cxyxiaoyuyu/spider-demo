import requests

# 响应的数据结构有
# text(字符串) content(二进制) json(对象)

# 爬取图片
if __name__ == "__main__":
  url = 'https://img.zcool.cn/community/01aa885f83bd3e11013e45842b77d7.jpg@1380w'
  headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
  }
  img_data = requests.get(url=url,headers=headers).content

  with open('./img.jpg','wb') as fp:
    fp.write(img_data)