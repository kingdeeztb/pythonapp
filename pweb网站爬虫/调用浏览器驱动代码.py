#coding=utf-8
import urllib.request
import random
from bs4 import BeautifulSoup
from io import BytesIO
import os
import time
import numpy as np
import pymysql
from selenium import webdriver
import requests

def time_update():
    time.sleep(0)
    time_new = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    return(time_new)

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='pymysql', charset='utf8')
#使用cursor方法创建一个游标
cursor = db.cursor()
 
browser = webdriver.Chrome()
browser.get('https://www.kele48.com/photo/photo_list.html?photo_type=21&page_index=1')

for i in range(1, 5):
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)

soup = BeautifulSoup(browser.page_source, "lxml")

# imgs = html.select("#new_list li img")
# browser.find_element_by_link_text("新闻").click() # 模拟鼠标点击文本为“新闻”的链接

#print(browser.current_url)  # https://www.baidu.com/
#print(browser.page_source)  # 获取网页源码

time.sleep(0)
browser.quit()  # 浏览器关闭


# def getContent(url,headers):
#     """
#     此函数用于抓取返回403禁止访问的网页
#     """
#     random_header = random.choice(headers)

#     """
#     对于Request中的第二个参数headers，它是字典型参数，所以在传入时
#     也可以直接将个字典传入，字典中就是下面元组的键值对应
#     """
#     req =urllib.request.Request(url)
#     req.add_header("User-Agent", random_header)
#     req.add_header("GET",url)
#     req.add_header("Host","www.3378778.com")
#     # req.add_header("Referer","http://www.3378778.com/html/3/category-catid-3.html")
 
#     content=urllib.request.urlopen(req).read()
#     return content
 
# url="http://www.3378778.com/html/3/category-catid-3.html"
# #这里面的my_headers中的内容由于是个人主机的信息，所以我就用句号省略了一些，在使用时可以将自己主机的User-Agent放进去
# my_headers = ["Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"]
# wbdata=getContent(url,my_headers)
# soup = BeautifulSoup(wbdata, 'lxml')

# https://www.kele48.com/

# 从解析文件中通过select选择器定位指定的元素，返回一个列表
news_titles = soup.select("div.box.movie_list>ul")
soup = BeautifulSoup(str(news_titles), "lxml")
news_titles = soup.select("a")
#print(news_titles)

# 1.定义数组将网页连接存入数组
# http://www.3378778.com/html/32/n-232-2.html
ww = []
for n in news_titles:
    # 提取出标题和链接信息
    # title = n.get_text().encode("latin1").decode("utf-8")#将读取的源码采用函数encode()转换为latin1编码，再将该编码转换为gbk，再利用发下代码
    title = n.get("title")
    link = "https://www.kele48.com"+n.get("href")
    data = {
    '标题':title,
    '链接':link
    }
    # print(link)
    # for i_url_page in range(1, 2):
    #     if i_url_page == 0 or i_url_page == 1:
    #         f_title=title,
    #         f_urls = link
    #     else:
    #         f_title=title,
    #         f_urls = link[0:-5]+'-'+str(i_url_page)+'.html'

            # #将数据写入数据库    
            # insert_newsinfo = ("INSERT INTO t_news_info(t_newstitle,t_newslink,t_newsediter,t_newscontect)" "VALUES(%s,%s,%s,%s)")
            # dese = (f_title,f_urls,'admin','')#变量的集合
            # cursor.execute(insert_newsinfo, dese)
            # db.commit()

    ww.append(link)
#print(ww)


# 2.提取连接中图片连接
qq = []
for k in ww:
    # print(k)
    url = k
    # print("url"+url)
    wbdata = requests.get(url).text
    soup = BeautifulSoup(wbdata, 'lxml')
    news_pic = soup.select("div.post_content>a")
    # print(news_pic)
    for q in news_pic:
        pic_src = q.get("src")
        data = {
            '图片链接': pic_src[0:-13]
        }
        print(data)
#         if pic_src[-7:-1] != 'slt.jp' and pic_src[-7:-1] != 'all.gi':
#             qq.append(pic_src)

# # 3.对连接图片进行下载
# os.makedirs('./image/', exist_ok=True)
# for pic_urls in qq:
#     print("正在下载..."+pic_urls)

#     for n in pic_urls:
#         time_update()
#         IMAGE_URL = pic_urls

#         def urllib_download():
#             from urllib.request import urlretrieve
#             urlretrieve(IMAGE_URL, './image/img1'+time_update()+'.jpg')
#     urllib_download()
# print("下载完成")