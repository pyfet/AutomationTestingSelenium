import os
import time
from helper import *
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Module():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

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
        drag_and_drop_by_offset(driver, locator("draggable3"), 50, 50)
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
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)
        
        move_to_module_page(driver, "datepicker.php")

        # tab 1
        move_to_next_frame(driver, 0, "#example-1-tab-1")
        datepicker = driver.find_element_by_id('datepicker').click()

        time.sleep(2)

        dateWidget = driver.find_element_by_id("ui-datepicker-div")
        rows = dateWidget.find_elements_by_tag_name("tr")
        columns = dateWidget.find_elements_by_tag_name("td")

        for cell in columns:
            if cell.text == '10':
                cell.find_element_by_link_text('10').click()
                time.sleep(2)
                break

        # tab 2
        move_to_next_frame(driver, 1, "#example-1-tab-2")
        for i in range(len(driver.find_elements_by_xpath("//select[@id='anim']/option"))):
            driver.find_elements_by_xpath("//select[@id='anim']/option")[i].click()
            time.sleep(1)
            datepicker = driver.find_element_by_id('datepicker').click()
            time.sleep(2)
            dateWidget = driver.find_element_by_id("ui-datepicker-div")
            rows = dateWidget.find_elements_by_tag_name("tr")
            columns = dateWidget.find_elements_by_tag_name("td")

            for cell in columns:
                if cell.text == '10':
                    cell.find_element_by_link_text('10').click()
                    time.sleep(2)
                    break

        # tab 3
        move_to_next_frame(driver, 2, "#example-1-tab-3")
        datepicker = driver.find_element_by_id('datepicker').click()
        time.sleep(2)
        driver.find_elements_by_xpath("//select[@class='ui-datepicker-month']/option")[3].click()
        time.sleep(1)
        driver.find_elements_by_xpath("//select[@class='ui-datepicker-year']/option")[3].click()
        time.sleep(1)
        dateWidget = driver.find_element_by_id("ui-datepicker-div")
        rows = dateWidget.find_elements_by_tag_name("tr")
        columns = dateWidget.find_elements_by_tag_name("td")

        for cell in columns:
            if cell.text == '10':
                cell.find_element_by_link_text('10').click()
                time.sleep(2)
                break

        # tab 4
        move_to_next_frame(driver, 3, "#example-1-tab-4")
        datepicker = driver.find_element_by_id('datepicker').click()
        time.sleep(2)
        dateWidget = driver.find_element_by_id("ui-datepicker-div")
        rows = dateWidget.find_elements_by_tag_name("tr")
        columns = dateWidget.find_elements_by_tag_name("td")

        for cell in columns:
            if cell.text == '10':
                cell.find_element_by_link_text('10').click()
                time.sleep(2)
                break

        for i in range(len(driver.find_elements_by_xpath("//select[@id='format']/option"))):
            driver.find_elements_by_xpath("//select[@id='format']/option")[i].click()
            time.sleep(1)

    def menu(self):
        #TODO: Implement tests for the menu module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)
        move_to_module_page(driver, "menu.php")
        move_to_next_frame(driver, 0, "#example-1-tab-1")
        time.sleep(3)
        
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)

        menu = driver.find_element_by_css_selector("#ui-id-2")
        actions.move_to_element(menu).perform()
        time.sleep(3)
        menu = driver.find_element_by_css_selector("#ui-id-3")
        actions.move_to_element(menu).perform()
        time.sleep(3)
        menu = driver.find_element_by_css_selector("#ui-id-4")
        actions.move_to_element(menu).perform()
        time.sleep(3)
        menu = driver.find_element_by_css_selector("#ui-id-3")
        actions.move_to_element(menu).perform()
        time.sleep(3)
        menu = driver.find_element_by_css_selector("#ui-id-2")
        actions.move_to_element(menu).perform()
        time.sleep(3)

        move_to_next_frame(driver, 0, "#example-1-tab-2")
        time.sleep(3)
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)

        #submenu = driver.find_element_by_css_selector("#ui-id-2")
        #action.move_to_element(submenu).perform()

        move_to_next_frame(driver, 0, "#example-1-tab-3")
        time.sleep(3)
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)
        
        



    def slider(self):
        #TODO: Implement tests for the slider module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)
        move_to_module_page(driver, "slider.php")
        move_to_next_frame(driver, 0, "#example-1-tab-1")
        time.sleep(3)
        slider = driver.find_element_by_css_selector("#slider-range-max > span")
        slider.click()
        slider.send_keys(Keys.RIGHT)
        time.sleep(2)
        slider.send_keys(Keys.RIGHT)
        time.sleep(2)
        slider.send_keys(Keys.RIGHT)
        time.sleep(2)
        slider.send_keys(Keys.RIGHT)
        time.sleep(2)
        slider.send_keys(Keys.LEFT)
        time.sleep(2)
        slider.send_keys(Keys.LEFT)
        time.sleep(2)
        slider.send_keys(Keys.RIGHT)
        time.sleep(2)
        

    def tabs(self):
        #TODO: Implement tests for the tabs module<span class="ui-slider-handle ui-state-default ui-corner-all" tabindex="0" style="left: 0%;"></span>
        driver = self.driver        
        authenticate(driver)
        time.sleep(3) 
        move_to_module_page(driver, "tabs.php")
        move_to_next_frame(driver, 0, "#example-1-tab-1")
        time.sleep(3)
        wait = WebDriverWait(driver, 10)
        

    def tooltip(self):
        #TODO: Implement tests for the tooltip module
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)

    # Frames and Windows
    def frames_and_windows(self):
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)
        move_to_module_page(driver, "frames-and-windows.php")

        #tab1
        move_to_next_frame(driver, 0, "#example-1-tab-1")
        time.sleep(1)
        driver.find_element_by_tag_name("a").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

        #tab2
    
        move_to_next_frame(driver, 1, "#example-1-tab-2")
        time.sleep(1)
        driver.find_element_by_tag_name("a").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

        #tab3
        move_to_next_frame(driver, 2, "#example-1-tab-3")
        time.sleep(1)
        driver.find_element_by_tag_name("a").click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

        #tab4
        move_to_next_frame(driver, 3, "#example-1-tab-4")
        time.sleep(1)
        driver.find_element_by_tag_name("a").click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)

    # Dynamic element
    def submit_button_clicked(self):
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)
        move_to_module_page(driver, "submit_button_clicked.php")

        #tab1
        move_to_next_frame(driver, 0, "#example-1-tab-1")
        bar = driver.find_element_by_tag_name('input')      
        bar.send_keys("start")
        time.sleep(1)      
        driver.find_element_by_name('submit').click()
        time.sleep(2)

        #tab2
        try:
            move_to_next_frame(driver, 0, "#example-1-tab-2")
            bar = driver.find_element_by_tag_name('input')      
            bar.send_keys("end")
            time.sleep(1)      
            driver.find_element_by_name('submit').click()
            time.sleep(2)
        except ElementNotInteractableException as error:
            print(error)


        #tab3
        try:
            move_to_next_frame(driver, 0, "#example-1-tab-3")
            bar = driver.find_element_by_tag_name('input')      
            bar.send_keys("complete")
            time.sleep(1)      
            driver.find_element_by_name('submit').click()
            time.sleep(2)
        except ElementNotInteractableException as error:
            print(error)

    def dropdown(self):
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)

        import random

        move_to_module_page(driver, "dropdown.php")

        # tab 1
        move_to_next_frame(driver, 0, "#example-1-tab-1")
        options = len(driver.find_elements_by_xpath("//select/option"))
        Select(driver.find_element_by_tag_name('select')).select_by_index(random.randint(0, options))
        time.sleep(1)

        # tab 2
        move_to_next_frame(driver, 1, "#example-1-tab-2")
        input_element = driver.find_element_by_tag_name("input")
        input_element.clear()
        input_element.send_keys("Cameroon")
        input_element.send_keys(Keys.RETURN)

        '''
        #module  has a problem
        time.sleep(2)
        driver.find_element_by_tag_name("a").click()
        driver.find_element_by_tag_name("ul").click()
        time.sleep(5)
        options = len(driver.find_elements_by_tag_name("li"))
        print(options)
        choice = lambda : driver.find_elements_by_tag_name("li")[(random.randint(0, options))]
        hover = ActionChains(driver).move_to_element(choice()).click().perform()
        time.sleep(1)'''

    # Registration
    def registration(self):
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)
        move_to_module_page(driver, "registration.php")

        file_path = os.path.abspath("assets/profile.jpeg")

        driver = driver.find_element_by_tag_name('form')
        driver.find_element_by_name('name').send_keys('Okonkwo')
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/section/div/div/div/form/fieldset/p[2]/input').send_keys("Ifeanyichukwu")
        time.sleep(1)
        driver.find_elements_by_css_selector("input[type='radio']")[0].click()
        time.sleep(1)
        driver.find_elements_by_css_selector("input[type='checkbox']")[1].click()
        time.sleep(1)
        driver.find_elements_by_css_selector("input[type='checkbox']")[2].click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[text()='India']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[text()='1']").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/section/div/div/div/form/fieldset/div[2]/select/*[text()='1']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[text()='2014']").click()
        time.sleep(1)
        driver.find_element_by_name("phone").send_keys("237658256324")
        time.sleep(1)
        driver.find_element_by_name("username").send_keys("wiseman")
        time.sleep(1)
        driver.find_element_by_name("email").send_keys("wiseman@email.com")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@type='file']").send_keys(file_path)
        time.sleep(1)
        driver.find_element_by_tag_name('textarea').send_keys("My name is Ifeanyi\nI am a student of FET in UB\nSpecialty is software \nI am in level 400\nThis is automation testing")
        time.sleep(1)
        driver.find_element_by_name("password").send_keys("setpassword")
        time.sleep(1)
        driver.find_element_by_name("c_password").send_keys("setpassword")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@value='submit']").click()
        time.sleep(3)

    # Alert
    def alert(self):
        driver = self.driver        
        authenticate(driver)
        time.sleep(3)
        move_to_module_page(driver, "alert.php")

        #tab1
        move_to_next_frame(driver, 0, "#example-1-tab-1")
        driver.find_element_by_tag_name('button').click()
        time.sleep(1)
        driver.switch_to_alert().accept()
        time.sleep(2)

        #tab2
        move_to_next_frame(driver, 1, "#example-1-tab-2")
        driver.find_element_by_tag_name('button').click()
        obj = driver.switch_to_alert()
        time.sleep(1)
        obj.send_keys("Okonkwo Ifeanyichukwu")
        time.sleep(1)
        obj.accept()
        time.sleep(3) 