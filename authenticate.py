from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

class Authenticate():
    def __init__(self, driver):
        self.driver = driver
        self.name = "pwemdcogb" + str(random.randint(0, 99999999))
        self.email =  "vmklmcsapw" + str(random.randint(0, 99999999)) + "@email.com"
        self.username = "mkwcpioqjf" + str(random.randint(0, 99999999))
        self.password = "nvuoda" + str(random.randint(0, 99999999))   

    def login(self):
        '''
        @param object driver
        '''
        driver = self.driver
        signin = driver.find_element_by_link_text("Signin")
        signin.click()

        username_element = driver.find_elements_by_name("username")[1]
        password_element = driver.find_elements_by_name("password")[1]

        username_element.send_keys(self.username)
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)

    def register(self):
        '''
        @param object driver
        '''
        driver = self.driver
        name_element = driver.find_element_by_name("name")
        phone_element = driver.find_element_by_name("phone")
        email_element = driver.find_element_by_name("email")
        city_element = driver.find_element_by_name("city")
        username_element = driver.find_elements_by_name("username")[1]
        password_element = driver.find_elements_by_name("password")[1]
        submit_button_element = driver.find_element_by_xpath("//input[@type='submit']")

        name_element.send_keys(self.name)
        phone_element.send_keys("124242234")
        email_element.send_keys(self.email)
        city_element.send_keys("Singapore")
        username_element.send_keys(self.username)
        password_element.send_keys(self.password+"\n")
        password_element.send_keys(Keys.RETURN)
