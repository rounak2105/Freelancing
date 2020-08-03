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

def reload():
    driver = webdriver.Firefox()
    driver.get("https://www.google.com/")
    actions = ActionChains(driver)
    actions.send_keys("Packers and Movers Goa")  #Google search keyword
    actions.perform()
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    search_results()

def search_results():
    RESULTS_LOCATOR = "TbwUpd.NJjxre"
    FINAL_RESULT = "www.indiabestpackersandmovers.in"
    CLICK_LOCATOR = "LC20lb.DKV0Md"
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, RESULTS_LOCATOR)))
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, CLICK_LOCATOR)))
    time.sleep(2)
    for i in range(10):
        val = driver.find_elements_by_class_name(RESULTS_LOCATOR)[i]
        cli = driver.find_elements_by_class_name(CLICK_LOCATOR)[i]
        print(i)
        print(val.text)
        if (FINAL_RESULT in val.text):
            cli.click()
            str = ['agartala','agra','ahmedabad','allahabad','banglore','mumbai','goa','bhopal','noida','mysore','vizag']
            time.sleep(60)          #Waiting on page for 1 minute
            driver.get("http://www.indiabestpackersandmovers.in/"+random.choice(str))
            driver.close()
            time.sleep(30*60)       #Restarting after 30 minutes
            reload()
            exit(0)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Next')]")))   #Loading next page
    time.sleep(5)
    driver.find_element_by_xpath("//span[contains(text(),'Next')]").click()
    search_results()


class Travel:
    global driver
    driver = webdriver.Firefox()
    driver.get("https://www.google.com/")
    actions = ActionChains(driver)
    actions.send_keys("Packers and Movers Goa")   #Google search keyword
    actions.perform()
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    search_results()





