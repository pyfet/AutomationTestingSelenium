from authenticate import *

def move_to_module_page(driver, href):
    '''
    @param object driver
    @param string href, link on anchor tag(<a>)
    '''
    driver.get("http://way2automation.com/way2auto_jquery/"+href)

def authenticate(driver):
    authenticate = Authenticate(driver)
    if "Registration Form" in driver.page_source:
        authenticate.register()
        if "Username or Password already exists." in driver.page_source:
            authenticate.login()