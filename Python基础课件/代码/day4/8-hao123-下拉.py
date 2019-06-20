from selenium import webdriver
import time
# 创建浏览器
driver = webdriver.Firefox()

# 访问好123
url = 'https://www.hao123.com/'
driver.get(url)

for i in range(100):
    # x管水平，y管垂直
    js = 'window.scrollTo(0,%s)'%(i*100)
    driver.execute_script(js)
    time.sleep(0.5)
    # js1= "var q=document.documentElement.scrollTop=0"
    # driver.execute_script(js1)

driver.quit()

