import os.path

import self
import time

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities.readProperties import ReadConfig


class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()

    def test_account_reg(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.hp.clickShop()
        self.hp.clickMyAccount()
        #self.hp.clickRegister()
        self.hp.clickLogin()
        #self.regpage = AccountRegistrationPage(self.driver)

        # self.regpage.setFirstName("Joyhkjk]n")
        # self.regpage.setLastName("Calkkhgtjlkjne")
        self.regpage.setEmail(ReadConfig.getUseremail())
        #self.email=randomeString.random_string_generator()+'@gmail.com'
        #self.regpage.setTelephone("65656565")
        #self.regpage.setPassword("abchhfgjd78xyz")
        #self.regpage.setConfirmPassword("abcxyz")
        #self.regpage.setPrivacyPolicy()
        #self.regpage.clickContinue()
        self.confmsg = self.regpage.getconfirmationmsg()
        #self.driver.close()
        if self.confmsg == 'Your Account Has Been Created!':
            screenshot_dir = os.path.join(r"C:\\", "Users", "MR.WICK", "PycharmProjects", "Opencart_V1", "screenshot")
            screenshot_path = os.path.join(screenshot_dir, "reg_page_passed01.png")

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            #assert True
            self.driver.close()
        else:
            screenshot_dir = os.path.join(r"C:\\", "Users", "MR.WICK", "PycharmProjects", "Opencart_V1", "screenshot")
            screenshot_path = os.path.join(screenshot_dir, "reg_page_failed.png")

            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)

