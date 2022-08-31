
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
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        username_field.click()
        username_field.send_keys("Admin")
        
        password_field.click()
        password_field.send_keys("admin123")
		
        login_button = self.driver.find_element(By.CLASS_NAME, "orangehrm-login-button")
        login_button.click()
        
        homepage_title = self.driver.find_element(By.CLASS_NAME, "oxd-topbar-header-breadcrumb-module").text
        self.assertEqual("PIM", homepage_title)