import time

from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.email_textbox = (By.CSS_SELECTOR, "input[name=email]")
        self.password_textbox = (By.CSS_SELECTOR, "input[name=password]")
        self.sign_in_button = (By.CSS_SELECTOR, "button.primary[type=submit]")
        self.create_and_account_link = (By.CSS_SELECTOR, "a[href='/account/register']")

    # Methods
    def clickOn_create_and_account(self):
        self.driver.find_element(*self.create_and_account_link).click()

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()
        time.sleep(2)



