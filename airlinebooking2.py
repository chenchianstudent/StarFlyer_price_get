#星月航空機票查詢  相關影片:https://www.youtube.com/watch?v=gCd3Fh9w3Do
#有用到google套件 Ruto - XPath Finder
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import time

url ='https://www.starflyer.jp/int_tw/'
browser=webdriver.Chrome('D:\webdriver\chromedriver')
browser.get(url) 

try:
    time.sleep(2)
    browser.find_element_by_xpath("//a[@class='js-aside is-devicePc']").click() # 按下預訂機票
    time.sleep(3)
    browser.find_element_by_xpath("(//button[@data-type='em']//span)[1]").click()  # 按下查詢
    time.sleep(5)
    elem = browser.page_source  # 擷取網頁該元素
finally:
    browser.quit()
    x = []
    soup = bs(elem,'html.parser')
    for i in soup.select('.days.clearfix'):
        sentence = i.text
        sentence = ''.join(sentence.split()) # 空白處理
        x.append(sentence)
print("去程機票價格")
print(x[0])
print("-------------------------------------------------------------------------------------------------------")
print("回程機票價格")
print(x[2])
