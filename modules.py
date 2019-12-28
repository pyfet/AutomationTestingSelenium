import time
from helper import *

class Module():
    def __init__(self, driver):
        self.driver = driver
        self.authenticate = Authenticate(self.driver)

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
        