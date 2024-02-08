import time

from selenium.webdriver.common.by import By
from ChallengeProject.POM.Data.productsData import Products

class ShopPage():

    def __init__(self,driver):
        self.driver = driver

#Locators
        self.shop_cart_icon = (By.CSS_SELECTOR, ".mini-cart-icon[href='/cart']")

    def click_On_Product(self, gender, productName):
        self.product_item = (By.CSS_SELECTOR, f"img[alt='{productName}']")
        self.driver.find_element(*self.product_item).click()
        time.sleep(2)

    def see_shop_chart(self):
        self.driver.find_element(*self.shop_cart_icon).click()
        time.sleep(2)











