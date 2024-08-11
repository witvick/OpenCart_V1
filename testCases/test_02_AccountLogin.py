import os.path

import self
import time

from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.Login_Page import Login_Page
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig




class Test_002_Login:

    baseURL = ReadConfig.getApplicationURL()




    def test_account_login(self, setup):
        self.driver = setup

        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.hp.clickShop()
        self.hp.clickMyAccount()

        self.hp.clickLogin()
        self.logpage = Login_Page(self.driver)

        self.logpage.Email()
        self.logpage.Password()
        time.sleep(20)


