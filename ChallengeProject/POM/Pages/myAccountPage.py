from selenium.webdriver.common.by import By

class MyAccountPage():

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.fullname_textlabel = (By.XPATH, "//div[@class='account-details-name flex gap-1']/div[2]")
        self.email_textlabel = (By.XPATH, "//div[@class='account-details-email flex gap-1']/div[2]")

    def get_full_name(self):
        fullname = self.driver.find_element(*self.fullname_textlabel).text
        return fullname
    def get_email(self):
        email = self.driver.find_element(*self.email_textlabel).text
        return email