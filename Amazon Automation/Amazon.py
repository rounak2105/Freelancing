from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import tkinter
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

#instock=https://www.amazon.com/AMD-Ryzen-3600-12-Thread-Processor/dp/B07STGGQ18/ref=lp_16225007011_1_3?s=computers-intl-ship&ie=UTF8&qid=1596225121&sr=1-3
#outstock=https://www.amazon.com/dp/B08BPKYL75/ref=twister_B07W6Y1YFC?_encoding=UTF8&psc=1

productLink = "https://www.amazon.com/AMD-Ryzen-3600-12-Thread-Processor/dp/B07STGGQ18/ref=lp_16225007011_1_3?s=computers-intl-ship&ie=UTF8&qid=1596225121&sr=1-3"
#productLink = "https://www.amazon.com/dp/B08BPKYL75/ref=twister_B07W6Y1YFC?_encoding=UTF8&psc=1"
uName = "fomibaf901@mailvk.net"
uPass = "123456"
maxPrice = 150

options = FirefoxOptions()
options.headless = False
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
driver = webdriver.Firefox(firefox_profile=firefox_profile, options=options)
driver.maximize_window()

while True:
    try:
        driver.get(productLink)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='buy-now-button']")))
        break
    except:
        print("Product not in stock")
        time.sleep(5)

price = driver.find_element_by_xpath("//span[@id='priceblock_ourprice']").text
driver.find_element_by_xpath("//input[@id='buy-now-button']").click()
print(price)
price = float(price[1:])
while True:
    if price < maxPrice:
        break
    else:
        print("Price is more than Max Price")
        time.sleep(5)
        driver.get(productLink)

actions = ActionChains(driver)
actions.send_keys(uName)
actions.perform()
driver.find_element_by_xpath("//input[@id='continue']").click()
actions = ActionChains(driver)
actions.send_keys(uPass)
actions.perform()
driver.find_element_by_xpath("//input[@id='signInSubmit']").click()
driver.find_element_by_xpath("//a[@class='a-declarative a-button-text ']").click()
driver.find_elements_by_xpath("//input[@type='submit']")[1].click()
