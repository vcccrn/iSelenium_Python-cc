# coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com") # 打开百度浏览器
driver.find_element_by_id("kw").send_keys("知乎") # 定位输⼊框并输⼊关键字
driver.find_element_by_id("su").click() #点击[百度⼀下]搜索
time.sleep(3) #等待3秒
driver.quit() #关闭浏览器