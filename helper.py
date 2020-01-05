import sys
import time
from authenticate import *
from selenium.common.exceptions import *

__saved_context__ = {}

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

def move_to(driver, element, click=False):
    '''
    Move to the element matched by selector or passed as argument.

    Parameters
    ----------
    element: str
        Any valid element
    click: bool
        Whether or not to click the element after hovering
        defaults to False
    '''
    try:
        action = webdriver.ActionChains(driver)
        action.move_to_element(element)
        if click:
            action.click(element)

        action.perform()
    except WebDriverException:
        print("move_to isn't supported with this browser driver.") 

def drag_and_drop(driver, element, target):
    '''
    Drags an element into another.

    Parameters
    ----------
    element: str
        source to search for. This can be any valid element.
        Element to be dragged.

    target: str
        target to search for. This can be any valid element
        Target element to be dragged into.

    '''
    webdriver.ActionChains(driver).drag_and_drop(element, target).perform()

def drag_and_drop_by_offset(driver, element, xoffset, yoffset):
    '''
    Drags an element into another.

    Parameters
    ----------
    element: str
        source to search for. This can be any valid element.
        Element to be dragged.

    xoffset: int
        x-coordinate of drop point

    yoffset: int
        y-coordinate of drop point

    '''
    webdriver.ActionChains(driver).drag_and_drop_by_offset(element, xoffset, yoffset).perform()

def click_and_hold(driver, element):
    webdriver.ActionChains(driver).click_and_hold(element).perform()

def move_by_offset(driver, xoffset, yoffset):
    webdriver.ActionChains(driver).move_by_offset(xoffset, yoffset)

def release(driver):
    webdriver.ActionChains(driver).release()

def move_to_next_frame(driver, frame_number, href):
    if "iframe" in driver.page_source:
        next_frame = lambda: driver.find_element_by_xpath("//a[@href='"+href+"']")
        next_frame().click()
        time.sleep(5)
        driver.switch_to.frame(frame_number)
        
    else:
        driver.switch_to.default_content()
        next_frame = lambda: driver.find_element_by_xpath("//a[@href='"+href+"']")
        next_frame().click()
        time.sleep(5)
        driver.switch_to.frame(frame_number)        

def getIds(driver):
    ids = lambda: driver.find_elements_by_xpath('//*[@id]')
    for ii in ids():
        #print ii.tag_name
        print(ii.get_attribute('id'))

def saveContext():
    __saved_context__.update(sys.modules[__name__].__dict__)

def restoreContext():
    names = sys.modules[__name__].__dict__.keys()
    for n in names:
        if n not in __saved_context__:
            del sys.modules[__name__].__dict__[n]
