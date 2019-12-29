import time
from helper import *

class Module():
    def __init__(self, driver):
        self.driver = driver
        self.authenticate = Authenticate(self.driver)

    # Interaction
    def draggable(self):
        #TODO: Implement tests for the draggable module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)  

    def droppable(self):
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)

        move_to_module_page(driver, "droppable.php")

        driver.switch_to.frame(0)
        
        element = driver.find_element_by_id("draggable")
        target = driver.find_element_by_id("droppable")
        
        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(element, target).perform()
        time.sleep(2)
        assert "Dropped!" in driver.page_source

        # Leave the frame
        driver.switch_to_default_content()

    def resizable(self):
        
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)
        
        move_to_module_page(driver, "resizable.php")

        driver.switch_to.frame(0)

        element = driver.find_element_by_css_selector("div.ui-resizable-handle:nth-child(4)")
 
        action_chains=ActionChains(driver)
        action_chains.click_and_hold(element).move_by_offset(200,200).release().perform()
        time.sleep(4)
        driver.switch_to_default_content() 
    
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
 