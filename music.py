# 爬取音乐
import requests

if __name__ == "__main__":
  url = 'https://m10.music.126.net/20201012223728/d9d1f9b04e46d3ddca1371d9a7615142/yyaac/obj/wonDkMOGw6XDiTHCmMOi/3932163564/fac6/1ece/faa9/2162e53e81abd52dd74bbf7feb2f5ddc.m4a'

  headers = {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
  music_data = requests.get(url=url,headers=headers).content

  with open('./music.mp4','wb') as fp:
    fp.write(music_data)