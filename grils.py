import requests
import re
from bs4 import BeautifulSoup as bs
import os

urls = ['/photography/','/campus/','/fresh/','/sweet/','/pure/','/youth/']
for v in urls:
 url = "https://www.vmgirls.com"
 headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
 html = requests.get(url+v,headers=headers).text
 jiexi = bs(html,'html.parser')
 #获取图片路径
 imgurl = jiexi.find_all('a',class_="list-title text-md h-2x")
     
 for i in imgurl:
  
  #访问图片库
  imges = requests.get(url+i['href'],headers=headers).text
  imgdown = bs(imges,"html.parser")
  
  #获取图片路径
  imgdowns = imgdown.find_all('img',alt="")

  
  
  for n,j in enumerate(imgdowns):
   ab = re.findall('.*?jpeg',j['src'])
   for urles in ab:
    print(urles+str(n)+str(n)+"...........................................................")
    print(i['title'])
    
    # 判断文件是否存在
    if os.path.exists(i['title']):
              
        print("文件夹已存在："+i['title'])

        #判断文件是否存在
        if os.path.exists(i['title']+'/'+i['title']+str(n)+".jpeg"):
                print("文件已存在1："+i['title']+'/'+i['title']+str(n)+".jpeg")        
        else:
            downimges = requests.get("https:"+urles,headers=headers).content
            with open(i['title']+"/"+i['title']+str(n)+".jpeg",'wb') as wr:
              print("正在下载"+i['title']+str(n)+".jpeg")
              wr.write(downimges)
    else:
      print("正在创建文件夹：")
      os.mkdir(i['title'])
      if os.path.exists(i['title']+"/"+i['title']+str(n)+".jpeg"):
         print("文件已存在："+i['title']+'/'+i['title']+str(n)+".jpeg")
                
      else:
         print("正在下载："+i['title']+"/"+i['title']+str(n)+".jpeg")
         downimges = requests.get("https:"+urles,headers=headers).content
        
         with open(i['title']+"/"+i['title']+str(n)+".jpeg",'wb') as wr:
          wr.write(downimges)
     