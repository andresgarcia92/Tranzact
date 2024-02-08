from selenium.webdriver.common.by import By

class CreateAccountPage():

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.fullname_textbox = (By.CSS_SELECTOR, "input[name=full_name]")
        self.email_textbox = (By.CSS_SELECTOR, "input[name=email]")
        self.password_textbox = (By.CSS_SELECTOR, "input[name=password]")
        self.sign_up_button = (By.CSS_SELECTOR, "button.primary[type=button]")

    # Methods
    def enter_fullname(self, fullname):
        self.driver.find_element(*self.fullname_textbox).send_keys(fullname)

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def create_account(self):
        self.driver.find_element(*self.sign_up_button).click()
