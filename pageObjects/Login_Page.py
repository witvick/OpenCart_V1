from selenium.webdriver.common.by import By

import time

from utilities.readProperties import ReadConfig


class Login_Page():
    mail_cont_xpath = "//*[@id='input-email']"
    pass_cont_xpath = "//*[@id='input-password']"


    def __init__(self, driver):
        self.driver = driver


    def Email(self):
        self.driver.find_element(By.XPATH,self.mail_cont_xpath).send_keys(ReadConfig.getUseremail())

    def Password(self):
        self.driver.find_element(By.XPATH,self.pass_cont_xpath).send_keys(ReadConfig.getPassword())