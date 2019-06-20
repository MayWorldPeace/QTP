from selenium import webdriver
driver = webdriver.Chrome()
url = 'http://baidu.com'
url2 = 'https://www.csdn.net'
driver.get(url)
driver.get(url2)
print("当前url:" + driver.current_url)
driver.back()
print("当前url:" + driver.current_url)