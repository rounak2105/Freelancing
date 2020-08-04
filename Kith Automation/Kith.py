from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

#instock=https://kith.com/products/nike-air-force-1-07-white
#outstock=https://kith.com/products/aaq47306

productName = "Nike Air Max React Red Pink Blue Galatic"
productLink = "https://kith.com/products/aaq47306"
eMail = "random@mail.com"
fName = "First"
lName = "Last"
uAddress = "111 Downtown"
uCity = "Vice City"
uZip = "99501"
uPhone = "9999999999"
cNo = "4444444444444444"
cName = fName+" "+lName
eDate = "05/22"
sCode = "111"

options = FirefoxOptions()
options.headless = False
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
driver = webdriver.Firefox(firefox_profile=firefox_profile, options=options)
driver.maximize_window()

driver.get("https://kith.com/")

#pop-up1
try:
 WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='glClose']")))
 driver.find_element_by_xpath("//span[@class='glClose']").click()
except:
 print("POP1 doesn't exsist")

#pop-up2
try:
 WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='needsclick DismissButton__closeButtonImage-spg526-0 kvcQJV kl-private-reset-css-Xuajs1']")))
 driver.find_element_by_xpath("//button[@class='needsclick DismissButton__closeButtonImage-spg526-0 kvcQJV kl-private-reset-css-Xuajs1']").click()
except:
 print("POP2 doesn't exsist")

#no-cookies
driver.find_element_by_xpath("//a[contains(text(),'I ACCEPT COOKIES')]").click()

#search-bar
"""
time.sleep(2)
driver.find_element_by_xpath("//a[@class='js-drawer-open-top']").click()
driver.find_element_by_xpath("//input[@id='Search-Drawer']").send_keys(productName)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()

#product-selection
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='snize-thumbnail']")))
driver.find_elements_by_xpath("//span[@class='snize-thumbnail']")[0].click()
"""

#add-to-cart
while(True):
 try:
  # user-link
  driver.get(productLink)
  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn product-form__add-to-cart']")))
  relay = driver.find_elements_by_xpath("//button[@class='btn product-form__add-to-cart']")[0]
  if("ADD TO CART" in relay.find_element_by_xpath("//span[@data-add-to-cart-text='']").text.upper()):
   print("Product is available, adding to cart ... ")
   driver.find_elements_by_xpath("//button[@class='btn product-form__add-to-cart']")[0].click()
   break
  else:
   print("Product cannot be added to cart, will be trying again in 0.5 seconds")
   time.sleep(0.5)
 except:
  print("Check your internet connection")
  exit(0)

time.sleep(5)
driver.get("https://kith.com/checkout")

while(True):
 try:
  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='continue_button']")))
  driver.find_element_by_xpath("//button[@id='continue_button']")
  break
 except:
  while (True):
   try:
    # user-link
    driver.get(productLink)
    WebDriverWait(driver, 10).until(
     EC.visibility_of_element_located((By.XPATH, "//button[@class='btn product-form__add-to-cart']")))
    relay = driver.find_elements_by_xpath("//button[@class='btn product-form__add-to-cart']")[0]
    if ("ADD TO CART" in relay.find_element_by_xpath("//span[@data-add-to-cart-text='']").text.upper()):
     print("Product is available, adding to cart ... ")
     driver.find_elements_by_xpath("//button[@class='btn product-form__add-to-cart']")[0].click()
     driver.get("https://kith.com/checkout")
     break
    else:
     print("Product cannot be added to cart, will be trying again in 0.5 seconds")
     time.sleep(0.5)
   except:
    print("Check your internet connection")
    exit(0)

#checkout-page
actions = ActionChains(driver)
actions.send_keys(eMail)
actions.perform()

#user-shipping
driver.find_element_by_xpath("//input[@id='checkout_shipping_address_first_name']").send_keys(fName)
driver.find_element_by_xpath("//input[@id='checkout_shipping_address_last_name']").send_keys(lName)
driver.find_element_by_xpath("//input[@id='checkout_shipping_address_first_name']").send_keys(fName)
driver.find_element_by_xpath("//input[@id='checkout_shipping_address_address1']").send_keys(uAddress)
driver.find_element_by_xpath("//input[@id='checkout_shipping_address_address2']").send_keys(uAddress)
driver.find_element_by_xpath("//input[@id='checkout_shipping_address_city']").send_keys(uCity)
driver.find_element_by_xpath("//input[@id='checkout_shipping_address_zip']").send_keys(uZip)
driver.find_element_by_xpath("//input[@id='checkout_shipping_address_phone']").send_keys(uPhone)

driver.find_element_by_xpath("//button[@id='continue_button']").click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='continue_button']")))

driver.find_element_by_xpath("//button[@id='continue_button']").click()

#user-payment
time.sleep(10)
driver.find_element_by_xpath("//input[@id='checkout_payment_gateway_128707719']").click()
actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.perform()
actions.send_keys(Keys.ENTER)
actions = ActionChains(driver)
actions.send_keys(cNo + Keys.TAB + cName + Keys.TAB + eDate + Keys.TAB + sCode)
actions.perform()



"""
seq = driver.find_elements_by_tag_name('iframe')
print("No of frames present in the web page are: ", len(seq))
for i in range(1 , 9):
 print(i)
 try:
  iframe = driver.find_elements_by_tag_name('iframe')[i]
  driver.switch_to.frame(iframe)
 except:
  print("Index isnt valid")
 try:
  driver.find_element_by_xpath("//input[@id='number']")
 except:
  print("Failed "+str(i))
"""
"""
driver.find_element_by_xpath("//input[@id='number']").send_keys(cNo)
driver.find_element_by_xpath("//input[@id='name']").send_keys(cName)
driver.find_element_by_xpath("//input[@id='expiry']").send_keys(eDate)
driver.find_element_by_xpath("//input[@id='verification_value']").send_keys(sCode)
driver.find_element_by_xpath("//button[@id='continue_button']").click()
"""
#if-card-failed
