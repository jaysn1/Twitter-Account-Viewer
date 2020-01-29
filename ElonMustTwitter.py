# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:26:31 2020

@author: Jaysn
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

user_name = "Enter_Your _Username"
password = "Enter_Your_Password"
search_text = "Elon Musk"


driver = webdriver.Chrome(executable_path=r"C:\Users\Jaysn\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://mobile.twitter.com/login")

try:
    WebDriverWait(driver, 20).until(lambda x: x.find_element_by_name('session[username_or_email]'))
    #WebDriverWait(driver, 20).until(lambda x: x.find_element_by_name('session[password]'))

except ():
    print('Not Found')
    exit()
user_name_field = driver.find_element_by_name("session[username_or_email]")
password_field = driver.find_element_by_name("session[password]")

user_name_field.send_keys(user_name)
password_field.send_keys(password, Keys.ENTER)

try:
    WebDriverWait(driver, 20).until(lambda x: x.find_element_by_css_selector('[aria-label="Search query"]'))
except ():
    print('Not Found')
    exit()
    
search_field = driver.find_element_by_css_selector('[aria-label="Search query"]')

search_field.send_keys(search_text, Keys.ENTER)

try:
    WebDriverWait(driver, 20).until(lambda x: x.find_element_by_xpath('//a[@href="/elonmusk"]'))
except ():
    print('Not Found')
    exit()

person_field = driver.find_element_by_xpath('//a[@href="/elonmusk"]')

person_field.click()