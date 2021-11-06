#coding=utf-8  
import urllib.request  
import urllib.error  
from bs4 import BeautifulSoup  
import time  
import socket  
  
socket.setdefaulttimeout(20)  # 设置socket层的超时时间为20秒  
header = {'User-Agent': 'Mozilla/5.0'}  
url = []  
# t = 'http://www.3378778.com/html/3/category-catid-3.html' 
t='http://www.4x4xrt.cc'
url.append(t)  
print(url)
  
for i in url:  
    request = urllib.request.Request(i, headers=header)  
    try:  
        response = urllib.request.urlopen(request)  
        soup = BeautifulSoup(response, 'html.parser')         
        title = soup.find('div', attrs={'class': 'fundDetail-tit'})  
        rate = soup.find('span', attrs={'id': 'gz_gszzl'})  
        print(title.text, rate.text)  
        response.close()    # 注意关闭response  
    except urllib.error.URLError as e:  
        print(e.reason)  
    time.sleep(1)   # 自定义  