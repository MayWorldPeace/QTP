from selenium import webdriver
import time


class OpenWindow(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def open(self, url):
        self.driver.get(url)
        time.sleep(2)

    def __del__(self):
        self.driver.quit()


if __name__ == '__main__':
    pass


