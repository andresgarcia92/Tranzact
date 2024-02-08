import random
import time

from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self,driver):
        self.driver = driver

#Locators
        self.login_icon = (By.CSS_SELECTOR, "#app a[href = '/account/login']")
        self.login_icon_loggedin = (By.CSS_SELECTOR, "#app a[href = '/account']")


#Methods
    def clickOn_login_icon(self):
         self.driver.find_element(*self.login_icon).click()

    def see_my_account(self):
        self.driver.find_element(*self.login_icon_loggedin).click()

    def select_gender(self):
        gender = ["men", "women"]
        selectedGender = random.choice(gender)
        return selectedGender
    def go_to_shopping_page(self, selectedGender):
        self.shop_link = (By.CSS_SELECTOR, f"a.nav-link[href='/{selectedGender}']")
        self.driver.find_element(*self.shop_link).click()
        time.sleep(5)



