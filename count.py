import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def total_modules(browser="webdriver.Firefox()"):
    driver = eval(browser)
    driver.set_window_size(1920, 1080)
    driver.get("https://www.way2automation.com/way2auto_jquery/index.php")
    no_modules = driver.find_elements_by_xpath("//div[@class='container margin-top-20']//li")
    driver.close()
    return len(no_modules)

def no_of_modules_in_section(browser="webdriver.Firefox()", section=None):
    section = int(section) - 1
    driver = eval(browser)
    driver.set_window_size(1920, 1080)
    driver.get("https://www.way2automation.com/way2auto_jquery/index.php")
    no_modules = driver.find_elements_by_xpath("//div[@class='container margin-top-20']//div[@class='linkbox margin-bottom-20']")
    no_modules = no_modules[section].find_elements_by_xpath(".//li")
    driver.close()
    return len(no_modules)

def get_key(val):
    options = json.load(open('section_options.json'))
    for key, value in options.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"
