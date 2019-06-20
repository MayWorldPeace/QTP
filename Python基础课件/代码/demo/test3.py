from selenium import webdriver
import time
driver = webdriver.Chrome()
# 设置url
url = 'http://baidu.com'
driver.get(url)
title = driver.title
page = driver.page_source
# 获取截图，存在内存中
driver.get_screenshot_as_file('aidu.png')
time.sleep(1)
driver.quit()