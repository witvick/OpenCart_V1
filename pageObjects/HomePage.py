from selenium.webdriver.common.by import By
import time

class HomePage:

    #lnk_shoping_kart_xpath= "//span[normalize-space()='Shopping Cart']"
    #lnk_myaccount_xpath = "/html/body/nav/div/div[2]/ul/li[2]/div/a/i[2]"
    lnk_register_xpath = "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[1]/a"
    lnk_login_xpath = "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[2]/a"

    def __init__(self, driver):

        self.driver = driver
        print(self.driver)

    def clickShop(self):
        time.sleep(10)
        shop=self.driver.find_element(By.XPATH,"//span[normalize-space()='Shopping Cart']")

        time.sleep(10)
        shop.click()
        time.sleep(10)

    def clickMyAccount(self):
        time.sleep(10)
        account=self.driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[2]/div/a/i[2]")
        time.sleep(5)
        account.click()


    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.lnk_register_xpath).click()



    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.lnk_login_xpath).click()

