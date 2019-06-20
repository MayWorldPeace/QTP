from selenium import webdriver
import time
# 浏览器驱动
driver = webdriver.Chrome()
# 访问地址
url = 'http://baidu.com'
driver.get(url)
# 定位输入框
el = driver.find_element_by_id('kw')
el.send_keys('hello')
cl = driver.find_element_by_xpath('//*[@id="su"]')
cl.click()
el_list = driver.find_elements_by_css_selector('div[id = "content_left"] > div > h3 >a')
for el in el_list:
    print(el.text, el.get_attribute('href'))

