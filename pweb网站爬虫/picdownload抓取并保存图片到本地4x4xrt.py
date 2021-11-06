# coding:utf-8

# 引入相关模块
import pymysql
import requests
import urllib.request
from bs4 import BeautifulSoup
from io import BytesIO
import os
import time
import numpy as np


def time_update():
    time.sleep(0)
    time_new = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    return(time_new)


def urllib_download():
    from urllib.request import urlretrieve
    urlretrieve(IMAGE_URL, './image/img1.png')


db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                     passwd='', db='pymysql', charset='utf8')
# 使用cursor方法创建一个游标
cursor = db.cursor()

# 查询数据库版本
cursor.execute("select version()")
data = cursor.fetchone()
print(" Database Version:%s" % data)

# 0.提取网站中内容详细连接
url = "http://www.4x4xrt.cc/"
# print(url)
# print(urls)
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
sleep_download_time = 2
time.sleep(sleep_download_time)  # 这里时间自己设定
wbdata = requests.get(url,headers=header).text
req = urllib.request.Request(url,headers=header)
request = urllib.request.urlopen(req)
request.close()  # 关闭请求 防止服务器拒绝服务

# 对获取到的文本进行解析
soup = BeautifulSoup(wbdata, 'lxml')
# 从解析文件中通过select选择器定位指定的元素，返回一个列表
news_titles = soup.select("div.index_new>div.new_list>ul>li>a")
news_title = soup.select("div.index_hit>div.hit_list>ul>li>a")
# print(news_titles)
# print(news_title)
# # 对返回的列表进行遍历

# 1.定义数组将网页连接存入数组
ww = []
for n in news_titles:
    # 提取出标题和链接信息
    # title = n.get_text().encode("latin1").decode("utf-8")#将读取的源码采用函数encode()转换为latin1编码，再将该编码转换为gbk，再利用发下代码
    title = n.get("title").encode("latin1").decode("gbk")
    link = "http://www.4x4xrt.cc"+n.get("href")

    # print(link)

    for i_url_page in range(1, 20):
        if i_url_page == 0 or i_url_page == 1:
            f_urls = link
        else:
            f_urls = link[0:-5]+'_'+str(i_url_page)+'.html'
        ww.append(f_urls)
# print(ww)


# 2.提取连接中图片连接
qq = []
for k in ww:
    # print(k)
    url = k
    # print("url"+url)
    wbdata = requests.get(url).text
    soup = BeautifulSoup(wbdata, 'lxml')
    news_pic = soup.select("a>img")
    # print(news_pic)
    for q in news_pic:
        pic_src = q.get("src")
        data = {
            '图片链接': pic_src
        }
        # print(data)
        if pic_src[-7:-1] != 'slt.jp' and pic_src[-7:-1] != 'all.gi':
            qq.append(pic_src)

# 3.对连接图片进行下载
os.makedirs('./image/', exist_ok=True)
for pic_urls in qq:
    print("正在下载..."+pic_urls)

    for n in pic_urls:
        time_update()
        IMAGE_URL = pic_urls

        def urllib_download():
            from urllib.request import urlretrieve
            urlretrieve(IMAGE_URL, './image/img1'+time_update()+'.jpg')
    urllib_download()
print("下载完成")


#     #将数据写入数据库
#     insert_newsinfo = ("INSERT INTO t_news_info(t_newstitle,t_newslink,t_newsediter,t_newscontect)" "VALUES(%s,%s,%s,%s)")
#     dese = (title,link,'admin','')#变量的集合
#     cursor.execute(insert_newsinfo, dese)
#     db.commit()

# # 前面省略，从下面直奔主题，举个代码例子：
# result2txt=str(data)          # data是前面运行出的数据，先将其转为字符串才能写入
# with open('北京自考网.txt','a') as file_handle:   # .txt可以不自己新建,代码会自动新建
# file_handle.write(result2txt)     # 写入
# file_handle.write('\n')         # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
# print("结果写入完成!!!")
