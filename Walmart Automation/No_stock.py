from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

def No_stock():
 #Checking if product in stock
 driver.get(url+"?selected=true")
 try:
  driver.find_element_by_class_name("prod-product-cta-add-to-cart.display-inline-block").click()
  #Update UI, product is available
  #Now we can execute Walmart.py
 except:
  #Product-not-available
  time.sleep(time_wait)
  #time_wait can be set to wait for any sepcified time
  No_stock()


firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
options = FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(firefox_profile=firefox_profile, options=options)
driver.maximize_window()
No_stock()