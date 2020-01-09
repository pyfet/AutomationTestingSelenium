import unittest
from modules import *

class AutomationTest(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)
        self.driver.get("http://way2automation.com/way2auto_jquery/index.php")
        self.module = Module(self.driver)
    
    def test_draggable(self):
        self.module.draggable()
    
    def test_droppable(self):
        self.module.droppable()

    def test_resizable(self):
        self.module.resizable()

    def test_datepicker(self):
        self.module.datepicker()

    def test_frames_and_windows(self):
        self.module.frames_and_windows()

    def test_submit_button_clicked(self):
        self.module.submit_button_clicked()

    def test_dropdown(self):
        self.module.dropdown()

    def test_registration(self):
        self.module.registration()

    def test_alert(self):
        self.module.alert()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
