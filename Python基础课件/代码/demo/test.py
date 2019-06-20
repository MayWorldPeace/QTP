from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# time.sleep(2)
# js = 'window.open("https://www.baidu.com");'
# driver.execute_script(js)
driver.set_window_size(400, 400)
driver.set_window_position(0, 0)
