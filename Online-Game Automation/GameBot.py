import tkinter
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.unleashedfear.com/'
user = 'Enter your username here by editing this'
pswd = 'Enter your username here by editing this'
options = Options()
options.headless = False
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get(url)

#Log-In
actions = ActionChains(driver)
actions.send_keys(user)
actions.perform()
actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.perform()
actions = ActionChains(driver)
actions.send_keys(pswd)
actions.perform()
actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.perform()
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()

#Skip-Loading
time.sleep(1)
driver.get("https://www.unleashedfear.com/alpha/?p=GENERAL.new_homepage")

#Crime-Page
WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'crimeurl')))
driver.find_element_by_id('crimeurl').click()

#Selecting-Elements
WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'form_crimes')))
dorm = driver.find_element_by_id("form_crimes")
form = dorm.find_element_by_class_name("midmargins")

for i in (1,10):
 ele_chance = form.find_element_by_xpath("//table/tbody/tr["+str(i)+"]/td[6]").text
 ele_strength = form.find_element_by_xpath("//table/tbody/tr["+str(i)+"]/td[8]").text
 print(ele_chance)
 print(ele_strength)
 time.sleep(10)
 
 #If Chance is 100% and Strength is Strong
 if(ele_chance=="100%" and ele_strength=="strong"):
     print("Yes")
     driver.fullscreen_window()
     if(i!=1):
      form.find_elements_by_xpath("//input[@type='radio']")[i-1].click()
     actions = ActionChains(driver)
     actions.send_keys(Keys.ENTER)
     actions.perform()
     actions = ActionChains(driver)
     actions.send_keys(Keys.ENTER)
     actions.perform()
     break;