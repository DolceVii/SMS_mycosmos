#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- coding: cp1253 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display

import time

try:
    chrome_options = Options()
    display = Display(visible=0, size=(1600, 1200))
    display.start()
    chrome_options.binary_location = '/usr/lib/chromium-browser/chromium-browser-v7'
    USERN = (By.NAME, '_user')
    PASSW = (By.NAME, '_pass')
    BTN1 = (By.ID, 'pr_area')
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)
    driver.implicitly_wait(10)
    
    driver.get('https://www.mycosmos.gr')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(USERN)).send_keys('USER LOGIN HERE')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(PASSW)).send_keys('PASSWORD HERE')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(PASSW)).send_keys(Keys.RETURN)
    time.sleep(1)
    
    TEL = (By.ID, '_to')
    MES = (By.ID, '_message')
    driver.get('https://www.mycosmos.gr/?_task=websms&_action=plugin.websms_compose')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(TEL)).send_keys('TEL NUMBER TO SEND')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(MES)).send_keys('MESSAGE TO SEND')
    driver.find_element_by_xpath("//input[@type='submit' and @value='Send']").click()
    time.sleep(1)
    
    driver.quit()
    display.stop()
except:
    print("Error")
