from selenium import webdriver
from time import sleep  # 这个后面会用到
# 创建Firefox驱动, 也可以按注释方法使用 headless 模式
# options = webdriver.firefox.options.Options()
# options.add_argument('-headless')
# driver = webdriver.Firefox(firefox_options=options)
driver = webdriver.Firefox()
# 打开搜狗微信网址
url = 'https://weixin.sogou.com/'
driver.get(url)

# 选择网页顶部的搜索组件
searchInput = driver.find_element_by_name('searchForm')
# 选择搜索组件中的输入框, 并输入关键字
searchInput.find_element_by_name('query').send_keys('零食')
# 选择搜索组件中的搜文件章按钮, 并模拟鼠标点击
searchInput.find_element_by_class_name('swz').click()

# 选择搜索结果
infoList = driver.find_element_by_css_selector('ul.news-list').find_elements_by_class_name('txt-box')
# 提取结果信息
result = []
# 保存当前标签页的句柄, 留做返回使用
mainHandle = driver.current_window_handle
for info in infoList:
    result.append({
        'title':info.find_element_by_tag_name('h3>a').text,
        'summary':info.find_element_by_tag_name('p').text,
    })
    # 模拟点击, 打开文章的新窗口
    info.find_element_by_tag_name('h3').click()
    # 切换浏览标签页到新窗口, 切换前需要等待下, 以便浏览器完成重定向
    sleep(3)
    driver.switch_to_window(driver.window_handles[1])
    # 保存当前浏览器标签页面的url
    result[-1]['url'] = driver.current_url
    print(result[-1])
    # 关闭当前标签页
    driver.close()
    # 返回原搜索结果的标签页
    driver.switch_to_window(mainHandle)