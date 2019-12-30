import time
from helper import *
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Module():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.authenticate = Authenticate(self.driver)

    # Interaction
    def draggable(self):
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)

        move_to_module_page(driver, "draggable.php")
        
        locator = lambda id : driver.find_element_by_id(id)

        # tab 1
        move_to_next_frame(driver, 0, "#example-1-tab-1")
        drag_and_drop_by_offset(driver, locator("draggable"), 150, 50)
        time.sleep(2)

        # tab 2
        move_to_next_frame(driver, 1, "#example-1-tab-2")
        drag_and_drop_by_offset(driver, locator("draggable"), 0, 50)
        time.sleep(1)
        drag_and_drop_by_offset(driver, locator("draggable2"), 50, 0)
        time.sleep(1)
        drag_and_drop_by_offset(driver, locator("draggable3"), 250, 250)
        time.sleep(1)
        drag_and_drop_by_offset(driver, locator("draggable5"), 50, 50)
        time.sleep(2)

        # tab 3
        move_to_next_frame(driver, 2, "#example-1-tab-3")
        drag_and_drop_by_offset(driver, locator("draggable"), 0, 150)
        time.sleep(1)
        drag_and_drop_by_offset(driver, locator("draggable2"), 150, 0)
        time.sleep(1)
        drag_and_drop_by_offset(driver, locator("draggable3"), 250, 250)
        time.sleep(2)

        # tab 4
        move_to_next_frame(driver, 3, "#example-1-tab-4")
        click_and_hold(driver, locator("draggable"))
        time.sleep(2)
        move_by_offset(driver, 200, 300)
        time.sleep(2)
        release(driver)
        time.sleep(2)

        # tab 5
        move_to_next_frame(driver, 4, "#example-1-tab-5")
        drag_and_drop_by_offset(driver, locator("draggable"), 0, 150)
        time.sleep(2)

    def droppable(self):
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)

        move_to_module_page(driver, "droppable.php")        
        locator = lambda id : driver.find_element_by_id(id)

        # tab 1
        move_to_next_frame(driver, 0, "#example-1-tab-1")
        drag_and_drop(driver, locator("draggable"), locator("droppable"))
        time.sleep(2)

        # tab 2
        move_to_next_frame(driver, 1, "#example-1-tab-2")
        drag_and_drop(driver, locator("draggable"), locator("droppable"))
        time.sleep(1)
        drag_and_drop_by_offset(driver, locator("draggable-nonvalid"), 50, 150)
        time.sleep(2)

        # tab 3
        move_to_next_frame(driver, 2, "#example-1-tab-3")
        drag_and_drop(driver, locator("draggable"), locator("droppable"))
        time.sleep(1)
        drag_and_drop(driver, locator("draggable"), locator("droppable-inner"))
        time.sleep(1)
        drag_and_drop(driver, locator("draggable"), locator("droppable2"))
        time.sleep(1)
        drag_and_drop(driver, locator("draggable"), locator("droppable2-inner"))
        time.sleep(1)

        # tab 4
        move_to_next_frame(driver, 3, "#example-1-tab-4")
        drag_and_drop(driver, locator("draggable"), locator("droppable"))
        time.sleep(1)
        drag_and_drop(driver, locator("draggable2"), locator("droppable"))
        time.sleep(2)

    def resizable(self):
        
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)
        
        move_to_module_page(driver, "resizable.php")
        

        handle ="#resizable > div.ui-resizable-handle:nth-child(4)"
        sideBar ="#resizable > div.ui-resizable-handle.ui-resizable-e"
        bottomBar="#resizable > div.ui-resizable-handle.ui-resizable-s"

        # tab 1
        move_to_next_frame(driver, 0, "#example-1-tab-1")
        element = driver.find_element_by_css_selector(sideBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(bottomBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(4)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver, element, -250, -250)
        time.sleep(4)

        # tab 2
        move_to_next_frame(driver, 1, "#example-1-tab-2")
        element = driver.find_element_by_css_selector(sideBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(bottomBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(4)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver, element, -250, -250)
        time.sleep(4)

        # tab 3
        move_to_next_frame(driver, 2, "#example-1-tab-3")
        element = driver.find_element_by_css_selector(sideBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(bottomBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver, element, -100, -100)
        time.sleep(4)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver,element,150,150)
        time.sleep(4)
        

        # tab 4
        move_to_next_frame(driver, 3, "#example-1-tab-4")
        element = driver.find_element_by_css_selector(sideBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(bottomBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(4)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver, element, -150, -150)
        time.sleep(4)

        # tab 5
        move_to_next_frame(driver, 4, "#example-1-tab-5")
        element = driver.find_element_by_css_selector(sideBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(bottomBar)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(3)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver,element,100,100)
        time.sleep(4)
        element = driver.find_element_by_css_selector(handle)
        drag_and_drop_by_offset(driver, element, -200, -200)
        time.sleep(4)

        
    
    def selectable(self):
        #TODO: Implement tests for the selectable module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3) 

    def sortable(self):
        #TODO: Implement tests for the sortable module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3) 

    # Widget
    def accordion(self):
        #TODO: Implement tests for the accordion module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3) 

    def autocomplete(self):
        #TODO: Implement tests for the autocomplete module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3) 

    def datepicker(self):
        #TODO: Implement tests for the datepicker module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3) 

    def menu(self):
        #TODO: Implement tests for the menu module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3) 

    def slider(self):
        #TODO: Implement tests for the slider module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3) 

    def tabs(self):
        #TODO: Implement tests for the tabs module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3) 

    def tooltip(self):
        #TODO: Implement tests for the tooltip module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)

    # Frames and Windows
    def frames_and_windows(self):
        #TODO: Implement tests for the frames and windows module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)

    # Dynamic element
    def submit_button_clicked(self):
        #TODO: Implement tests for the submit button clicked module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)

    def dropdown(self):
        #TODO: Implement tests for the dropdown module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)

    # Registration
    def registration(self):
        #TODO: Implement tests for the registration module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)

    # Alert
    def alert(self):
        #TODO: Implement tests for the alert module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)
 