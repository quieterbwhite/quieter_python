# -*- coding=utf-8 -*-
# Created Time: 2018年08月07日 星期二 14时20分55秒
# File Name: 01_quickstart.py

#导入webdriver
from selenium import webdriver
import time

#调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.PhantomJS()
#driver.set_window_size(1366, 768)
#如果没有在环境变量指定PhantomJS位置
#driver = webdriver.PhantomJS(executable_path = "./phantomjs")

#get方法会一直等到页面加载，然后才会继续程序，通常测试会在这里选择time.sleep(2)

driver.get("http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+3+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E8%A1%8C%E6%94%BF%E6%A1%88%E4%BB%B6")

#获取页面名为wraper的id标签的文本内容
#data = driver.find_element_by_id('wrapper').text

#打印数据内容
#print(data)

#print driver.title

#生成页面快照并保存
#driver.save_screenshot("baidu.png")

# id="kw"是百度搜索输入框，输入字符串"长城"
#driver.find_element_by_id('kw').send_keys(u'长城')

# id="su"是百度搜索按钮，click()是模拟点击
#driver.find_element_by_id('su').click()

#获取新的页面快照
#driver.save_screenshot("长城.png")

#打印网页渲染后的源代码
#print(driver.page_source)

#获取当前页面Cookie
print(driver.get_cookies())

js = """
    var data = getKey();
    return data;
"""

print(driver.execute(console.log(vl5x)))

driver.close()
