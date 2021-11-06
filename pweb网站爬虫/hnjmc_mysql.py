# coding:utf-8

# 引入相关模块
import pymysql
import requests
import urllib.request
from bs4 import BeautifulSoup

db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                     passwd='', db='pymysql', charset='utf8')
# 使用cursor方法创建一个游标
cursor = db.cursor()

for url in range(1, 87):
    if url == 1:
        url = "index"
        urls = "http://www.hceb.edu.cn/xxxw/"+str(url)+".html"
    else:
        urls = "http://www.hceb.edu.cn/xxxw/"+str(url)+".html"
    print(url)
    wbdata = requests.get(urls).text
    # 对获取到的文本进行解析
    soup = BeautifulSoup(wbdata, 'lxml')
    # 从解析文件中通过select选择器定位指定的元素，返回一个列表
    news_titles = soup.select("div.m_lik.m_new1.bd.newb>ul>li>a")
    # print(news_titles)
    # 对返回的列表进行遍历
    for n in news_titles:
        # 提取出标题和链接信息
        # 将读取的源码采用函数encode()转换为latin1编码，再将该编码转换为gbk，再利用发下代码
        title = n.get_text().encode("latin1").decode("gbk")
        link = n.get("href")
        data = {
            '标题': title,
            '链接': link
        }
        for all_links in link:
            all_urls = link
            response = urllib.request.urlopen(all_urls)
            html = str(response.read(), 'gbk')
            soup = BeautifulSoup(html, 'lxml')
            news_contect = soup.select("dl.k32")
            for n in news_contect:
                news_contects = n.get_text()
        print(title)
        print(link)
        print(news_contects)
        # # 将数据写入数据库
        # insert_newsinfo = (
        #     "INSERT INTO t_news_info(t_newstitle,t_newslink,t_newsediter,t_newscontect)" "VALUES(%s,%s,%s,%s)")
        # dese = (title, link, 'admin', '')  # 变量的集合
        # cursor.execute(insert_newsinfo, dese)
        # db.commit()

'''  
        file_handle=open('1.txt',mode='w')
        file_handle.write(news_contects) 
url="http://www.hceb.edu.cn/2005/xxxw_0809/77.html"
response = urllib.request.urlopen(url)
html =str(response.read(),'gbk')
#print(html)
soup = BeautifulSoup(html,'lxml')
news_contect = soup.select("dl.k32")
for n in news_contect:
    news_contects=n.get_text()
    print(news_contects)
    
'''
# print(urls)
# 请求腾讯新闻的URL，获取其text文本
#wbdata = requests.get(html).text
# 对获取到的文本进行解析
#soup = BeautifulSoup(html,'lxml')
# 从解析文件中通过select选择器定位指定的元素，返回一个列表
#news_contect = soup.select("dl.k32>div.lnmu>ul")
# news_contect_2 = soup.select("dl.k32>div.listn.imgk")
# for n in news_contect:
# news_contects=n.get_text()
# print(news_contects)
# for m in news_contect_2:
# news_contects_2=m.get_text().encode('gbk','ignore')
# print(str(news_contects_2.read(),'utf-8'))
'''
# 对返回的列表进行遍历
for n in news_titles:
# 提取出标题和链接信息
    title = n.get_text().encode("latin1").decode("gbk")#将读取的源码采用函数encode()转换为latin1编码，再将该编码转换为gbk，再利用发下代码
    link = n.get("href")
    data = {
    '标题':title,
    '链接':link
    }
    print(data)
'''
