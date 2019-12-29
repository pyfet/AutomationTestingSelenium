import unittest
from modules import *

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1920, 1080)        
        self.driver.get("http://way2automation.com/way2auto_jquery/index.php")
        self.module = Module(self.driver)

    def test_draggable(self):
        module = self.module
        module.droppable()

    def test_resizable(self):
        module = self.module
        module.resizable()    

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()