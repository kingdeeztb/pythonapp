# coding:utf-8

# 引入相关模块
import requests
from bs4 import BeautifulSoup
for url in range(0, 87):
    if url == 1:
        url = "index"
        urls = "http://www.hceb.edu.cn/xxxw/"+str(url)+".html"
    else:
        urls = "http://www.hceb.edu.cn/xxxw/"+str(url)+".html"
    print(url)
# print(urls)
    # 请求腾讯新闻的URL，获取其text文本
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
        print(data)
