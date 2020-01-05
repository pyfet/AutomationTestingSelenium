import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

name = "Desmond" + str(random.randint(1000000, 99999999))
password = "DesmondMiles" + str(random.randint(1000000, 99999999))
username = "Miles" + str(random.randint(1000000, 99999999))

def login(driver):
    signin = driver.find_element_by_link_text("Signin")
    time.sleep(2)
    signin.click()
    time.sleep(2)
    username_element = driver.find_elements_by_name("username")[1]
    time.sleep(2)
    password_element = driver.find_elements_by_name("password")[1]
    time.sleep(2)

    username_element.send_keys(username)
    time.sleep(2)
    password_element.send_keys(password)
    time.sleep(2)
    password_element.send_keys(Keys.RETURN)


def register(driver):    
    name_element = driver.find_element_by_name("name")
    phone_element = driver.find_element_by_name("phone")
    email_element = driver.find_element_by_name("email")
    city_element = driver.find_element_by_name("city")
    username_element = driver.find_elements_by_name("username")[1]
    password_element = driver.find_elements_by_name("password")[1]
    submit_button_element = driver.find_element_by_xpath("//input[@type='submit']")

    name_element.send_keys("Desmond")
    time.sleep(2)
    phone_element.send_keys("124242234")
    time.sleep(2)
    email_element.send_keys("desmond@email.com")
    time.sleep(2)
    city_element.send_keys("Singapore")
    time.sleep(2)
    username_element.send_keys(username)
    time.sleep(2)
    password_element.send_keys(password)
    time.sleep(2)
    password_element.send_keys(Keys.RETURN)


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
    '''
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
    '''
    def test_draggable(self):
        driver = self.driver
        driver.get("http://way2automation.com/way2auto_jquery/index.php")

        time.sleep(2)
        if "Registration Form" in driver.page_source:
            register(driver)
            if "Username or Password already exists." in driver.page_source:
                time.sleep(10)
                login(driver)

        
        time.sleep(2)
        for handle in driver.window_handles:
            driver.switch_to_window(handle)
        time.sleep(20)
        element = driver.find_element_by_id("draggable")
        
        target = driver.find_element_by_id("droppable")
        action_chains = ActionChains(driver)
        print(type(action_chains.drag_and_drop(element, target).perform()))
        time.sleep(2)
        assert "Dropped!" in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()