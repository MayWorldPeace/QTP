from selenium import webdriver
import time
driver = webdriver.Chrome()
url = 'http://baidu.com'
driver.get(url)
data = driver.get_cookies()
print(data)