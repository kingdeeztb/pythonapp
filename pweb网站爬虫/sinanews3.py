# -*- coding:utf8 -*-

# import urllib.request
# import sys
# reload(sys)
# sys.setdefaultencoding("gbk")

# req = urllib.request.Request("http://www.hceb.edu.cn/2005/xxxw_0809/77.html")
# res = urllib.request.urlopen(req)
# html = res.read()
# res.close()

# html = unicode(html, "gb2312").encode("utf8")  #gb2312--->utf-8
# print(html)


import urllib.request

response = urllib.request.urlopen(
    'http://www.hceb.edu.cn/2005/xxxw_0809/77.html')

html = str(response.read(), 'gbk')

print(html)
