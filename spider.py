from bs4 import BeautifulSoup # 网页解析 获取数据
import re   # 正则表达式 进行文字匹配
import urllib.request,urllib.error  # 制定URL 获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行 SQLite 数据库操作


# 全局正则
findLink = re.compile(r'<a href="(.*?)">')   # 创建正则表达式对象
findImg = re.compile(r'<img.*src="(.*?)"',re.S)  # re.S 忽视换行符
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)


def main():
  baseUrl = 'https://movie.douban.com/top250?start='
  savePath = '.\\douban_movie_top250.xls'

  # 1 爬取网页
  dataList = getData(baseUrl)
  # for data in dataList:
  #   print(data)
  #   print('-'*90)

  # 2 保存数据
  saveData(dataList,savePath)

# 爬取网页
def getData(baseUrl):
  dataList = []
  for i in range(0,10):  # 调用获取页面信息的函数 10次 每次25个
    url = baseUrl + str(i*25)
    html = askURL(url)
    # 逐一解析数据
    soup = BeautifulSoup(html,'html.parser')
    for item in soup.find_all('div',class_="item"):   # 查找符合要求的字符串 形成列表
      # print(item) 
      data = []  # 保存一部电影的所有信息
      item = str(item)

      # 链接
      link = re.findall(findLink,item)[0]   # 影片详情链接
      data.append(link)

      # 图片
      imgSrc = re.findall(findImg,item)[0]
      data.append(imgSrc)

      # title
      titles = re.findall(findTitle,item)
      if len(titles) > 1:
        data.extend(titles)
      else: 
        data.append(titles[0])
        data.append('')

      # 评分
      rating = re.findall(findRating,item)[0]
      data.append(rating)

      # 评价人数
      judgeNum = re.findall(findJudge,item)[0]
      data.append(judgeNum)

      # inq 概述
      inq = re.findall(findInq,item)
      if len(inq) > 0:
        data.append(inq[0])
      else:
        data.append('')

      # bd
      bd = re.findall(findBd,item)[0]
      bd = re.sub('<br(\s+)?/>(\s+)',' ',bd)  
      bd = re.sub('/',' ',bd)   # 去掉 /
      data.append(bd.strip())

      dataList.append(data)

  return dataList


# 得到一个指定url的网页内容
def askURL(url):
  head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
  }
  request = urllib.request.Request(url=url,headers=head)
  try: 
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
  except urllib.error.URLError as e:
    if hasattr(e,'code'):
      print(e.code)
    if hasattr(e,'reason'):
      print(e.reason)
  return html


def saveData(dataList,savePath):
  print('...现在开始保存数据...')
  book = xlwt.Workbook(encoding='utf-8',style_compression=0)
  sheet = book.add_sheet('豆瓣电影top250',cell_overwrite_ok=True)
  col = ('电影详情链接','图片链接','影片中文名','影片英文名','评分','评价数','概述','描述信息')
  for i in range(len(col)):
    sheet.write(0,i,col[i])  # 写入第一行

  for i in range(len(dataList)):
    data = dataList[i]
    for j in range(0,len(col)):
      sheet.write(i+1,j,data[j])

  book.save('./doubanTop250.xls')


if __name__ == "__main__":
  main()