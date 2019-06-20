from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
url = 'http://baidu.com'
driver.get(url)
el = driver.find_element_by_name('wd')
# el = driver.find_element(By.ID, 'kw')
el.send_keys('hello')
cl = driver.find_element_by_xpath('//*[@id="su"]')
# cl = driver.find_element(By.ID, 'su')
cl.click()
