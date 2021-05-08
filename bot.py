import random
import selenium
from selenium import webdriver
import time
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.keys import Keys
from parsel import Selector
from lxml import html
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from details import *

def login():
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    browser = webdriver.Chrome(chrome_options=option,executable_path='C:/Users/Hiveminds/Desktop/Work/honey/chromedriver.exe')
    url = "https://www.instagram.com"
    browser.get(url)
    time.sleep(2)

    browser.find_element_by_xpath('//input[@name="username"]').send_keys(user)
    time.sleep(1)
    browser.find_element_by_xpath('//input[@name = "password"]').send_keys(password)
    time.sleep(2)
    browser.find_element_by_xpath('//button[@type = "submit"]').click()
    time.sleep(5)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    time.sleep(5)
    browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

def like_comment():
    browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(search_term)
    time.sleep(3)
    browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a').send_keys(Keys.ENTER)
    time.sleep(5)
    url_list=[]
    time.sleep(5)
    elems = browser.find_elements_by_tag_name('a')
    time.sleep(5)
    for elem in elems:
        href = elem.get_attribute('href')
        if href is not None:
            url_list.append(href)
    links = [k for k in url_list if '.com/p' in k]  ## all the links of the pics to be liked and commented

    for link in links:
        time.sleep(1)
        browser.get(link)
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
        time.sleep(3)
        browser.find_element_by_class_name('X7cDz').click()
        time.sleep(3)
        try:
            browser.find_element_by_xpath('//textarea[@placeholder="Add a comment…"]').send_keys(random.choice(comment))
            time.sleep(2)
        except:
            pass
        try:
            browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]').click()
            time.sleep(2)
        except:
            pass

def main():
    log = login()
    LandC = like_comment()

if __name__ == '__main__':
    main()
