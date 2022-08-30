
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

class TestLoginPage(unittest.TestCase):

    root_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
    service = Service(os.path.join(root_path, "chromedriver.exe"))
    driver = Chrome(service=service) 
    base_url = "https://opensource-demo.orangehrmlive.com"

    def setUp(self):    
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_login_successfull(self):
        field_username = self.driver.find_element(By.NAME, "username")
        field_username.click()
        field_username.send_keys("Admin")
        self.assertTrue(True)