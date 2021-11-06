# coding:utf-8

# 引入相关模块
import pymysql
import requests
from bs4 import BeautifulSoup

db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                     passwd='', db='pymysql', charset='utf8')
# 使用cursor方法创建一个游标
cursor = db.cursor()

url = "http://toutiao.sogou.com/"
# print(url)
# print(urls)
# 请求腾讯新闻的URL，获取其text文本
wbdata = requests.get(url).text
# 对获取到的文本进行解析
soup = BeautifulSoup(wbdata, 'lxml')
# 从解析文件中通过select选择器定位指定的元素，返回一个列表
news_titles = soup.select("div.list-mod")
news_title = soup.select("div.list-mod>ul>li>a")
# print(news_title)
# 对返回的列表进行遍历
for n in news_title:
    # 提取出标题和链接信息
    # title = n.get_text().encode("latin1").decode("utf-8")#将读取的源码采用函数encode()转换为latin1编码，再将该编码转换为gbk，再利用发下代码
    title = n.get("title").encode("latin1").decode("utf-8")
    link = n.get("href")
    data = {
        '标题': title,
        '链接': link
    }
    print(data)
    # 将数据写入数据库
    insert_newsinfo = (
        "INSERT INTO t_news_info(t_newstitle,t_newslink,t_newsediter,t_newscontect)" "VALUES(%s,%s,%s,%s)")
    dese = (title, link, 'admin', '')  # 变量的集合
    cursor.execute(insert_newsinfo, dese)
    db.commit()

    # # 前面省略，从下面直奔主题，举个代码例子：
    # result2txt=str(data)          # data是前面运行出的数据，先将其转为字符串才能写入
    # with open('结果存放.txt','a') as file_handle:   # .txt可以不自己新建,代码会自动新建
    # file_handle.write(result2txt)     # 写入
    # file_handle.write('\n')         # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
    # print("结果写入完成!!!")
