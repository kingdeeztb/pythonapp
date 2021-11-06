'''
import requests
import time
import re
se = requests.session()
 
if __name__ == '__main__':
    Post_url = "http://c.m.163.com/nc/article/headline/T1348649580692/0-40.html" #自己想办法弄到key
    Post_data = {
        'wenzhang': '床前明月光，疑是地上霜。'
    }
    Text = se.post(Post_url, data=Post_data).text.replace("'", '"').replace('/ ', '/')
    print(Text)
    from multiprocessing.dummy import Pool as ThreadPool

# 使用map实现多线程爬虫
pool = ThreadPool(4)
pool.map(crawler_func, data_list)
pool.close()
pool.join()
————————————————
版权声明：本文为CSDN博主「请叫我子鱼」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/xiang12835/java/article/details/89083620
'''    
# 请求库
import requests
# 用于解决爬取的数据格式化
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# 爬取的网页链接
r= requests.get("http://c.m.163.com/nc/article/headline/T1348649580692/0-40.html")
# 类型
# print(type(r))
print(r.status_code)
# 中文显示
# r.encoding='utf-8'
r.encoding=None
print(r.encoding)
#print(r.text)
result = r.text
   
html = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.p.contents)
