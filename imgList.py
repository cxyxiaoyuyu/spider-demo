import requests
import re
import os

# 爬取一整张页面的图片
if __name__ == "__main__":
    # 创建一个文件夹 保存图片
    if not os.path.exists('imgLib'):
        os.mkdir('imgLib')
    
    url = 'https://www.qiushibaike.com/imgrank/page/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    regxp = '<div class="thumb">.*?<img src="(.*?)" alt.*?></div>'

    for pageNum in range(1,5):
        new_url = url + str(pageNum)
        page_text = requests.get(url=new_url,headers=headers).text

        img_src_list = re.findall(regxp,page_text,re.S)
        print('开始保存第%d页图片'%pageNum)
        for src in img_src_list:
            src = 'https:' + src  # 拼接完整的url
            img_data = requests.get(url=src,headers=headers).content
            # 生成图片名称
            img_name = src.split('/')[-1]
            img_path = './imgLib/'+img_name
            
            with open(img_path,'wb') as fp:
                fp.write(img_data) 
                print(img_name,'下载成功')


