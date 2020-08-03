from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


#out-stock=https://www.walmart.com/ip/Lol-Surprise-Girls-We-Run-The-World-Backpack/712590528
#in-stock=https://www.walmart.com/ip/onn-Bluetooth-On-Ear-Headphones-Black/368708375



fName = ""
lName = ""
addL  = ""
phone = ""
cNum  = ""
cMont = ""
cYear = ""


options = FirefoxOptions()
options.headless = True
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
driver = webdriver.Firefox(firefox_profile=firefox_profile,options=options)
driver.maximize_window()

#Getting the walmart site
driver.get(url+"?selected=true")

#add-to-cart
driver.find_element_by_class_name("prod-product-cta-add-to-cart.display-inline-block").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "new-ny-styling.cart-pos-proceed-to-checkout")))
driver.get("https://www.walmart.com/checkout")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-automation-id='new-guest-continue-button']")))
driver.find_element_by_xpath("//button[@data-automation-id='new-guest-continue-button']").click()
try:
 WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-automation-id='fulfillment-method-unavailable']")))
 print(driver.find_element_by_xpath("//div[@data-automation-id='fulfillment-method-unavailable']").text)
 exit(0)
except:
 WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-automation-id='fulfillment-continue']")))
 driver.find_element_by_xpath("//button[@data-automation-id='fulfillment-continue']").click()

#filling-details
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='firstName']")))
driver.find_element_by_xpath("//input[@id='firstName']").send_keys(fName);
driver.find_element_by_xpath("//input[@id='addressLineOne']").send_keys(addL);
driver.find_element_by_xpath("//input[@id='lastName']").send_keys(lName);
driver.find_element_by_xpath("//input[@id='phone']").send_keys(phone);
driver.find_element_by_xpath("//input[@id='email']").send_keys(eMail);
driver.find_element_by_xpath("//button[@data-automation-id='address-book-action-buttons-on-continue']").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-automation-id='address-validation-message-save-address']")))
driver.find_element_by_xpath("//button[@data-automation-id='address-validation-message-save-address']").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='creditCard']")))
time.sleep(2)
driver.find_element_by_xpath("//input[@id='creditCard']").send_keys(cNo)
time.sleep(2)
driver.find_element_by_xpath("//select[@id='month-chooser']").click()
time.sleep(2)

i=0
#filing-month
if(mont<10):
 while i < mont :
  i+=1
  actions = ActionChains(driver)
  actions.send_keys("0")
  actions.perform()
else:
 while i < mont-9 :
  i+=1
  actions = ActionChains(driver)
  actions.send_keys("1")
  actions.perform()


actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.perform()
time.sleep(2)
driver.find_element_by_xpath("//select[@id='year-chooser']").click()

i=0
#filing-year
while i < year-2020:
 i+=1
 actions = ActionChains(driver)
 actions.send_keys("2")
 actions.perform()

actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.perform()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='cvv']").send_keys("222")
time.sleep(2)
driver.find_element_by_xpath("//button[@data-automation-id='save-cc']").click()

#check-card
try:
 WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-automation-id='summary-place-holder']")))
except:
 print("Card Declined ")
 exit(0)

driver.find_element_by_xpath("//button[@data-automation-id='summary-place-holder']").click()
print("Successful Checkout")
