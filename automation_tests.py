import time
import unittest
from modules import *

class AutomationTest(unittest.TestCase):

    def setUp(self):
        self.startTime = time.time()
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

    def test_sortable(self):
        self.module.sortable()

    def test_datepicker(self):
        self.module.datepicker()
    
    def test_tooltip(self):
        self.module.tooltip()

    def test_menu(self):
        self.module.menu()

    def test_slider(self):
        self.module.slider()

    def test_tabs(self):
        self.module.tabs()

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

    def test_selectable(self):
        self.module.selectable() 

    def test_accordion(self):
        self.module.accordion()

    def test_autocomplete(self):
        self.module.autocomplete() 

    def tearDown(self):
        self.driver.close()
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))
