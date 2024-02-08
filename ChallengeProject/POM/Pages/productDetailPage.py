import random
import time
from faker import Faker
from selenium.webdriver.common.by import By

class ProductDetailPage():

    def __init__(self,driver):
        self.driver = driver

        #locators

        self.quantity_textbox = (By.CSS_SELECTOR, "input[name=qty]")

        self.sizeM_option = (By.XPATH, "//ul[@class='variant-option-list flex justify-start gap-05 flex-wrap']//a[text()='M']")

        self.sizeL_option = (By.XPATH, "//ul[@class='variant-option-list flex justify-start gap-05 flex-wrap']//a[text()='M']")

        self.colorBlack_option = (By.XPATH, "//ul[@class='variant-option-list flex justify-start gap-05 flex-wrap']//a[text()='Black']")

        self.colorWhite_option = (By.XPATH, "//ul[@class='variant-option-list flex justify-start gap-05 flex-wrap']//a[text()='White']")

        self.add_to_cart_button = (By.CSS_SELECTOR, "button.button.primary")

        self.continue_shopping_link = (By.CSS_SELECTOR, ".add-cart-popup-continue")

        #Methods

    def enter_quantity(self):
        randomQuantity = str(random.randint(1, 10))
        self.driver.find_element(*self.quantity_textbox).clear()
        self.driver.find_element(*self.quantity_textbox).send_keys(randomQuantity)
        return randomQuantity

    def select_size(self, productSize):
        self.size_option = (By.XPATH, f"//ul[@class='variant-option-list flex justify-start gap-05 flex-wrap']//a[text()='{productSize}']")

        self.driver.find_element(*self.size_option).click()
        time.sleep(2)

    def select_color(self, productColor):
        self.color_option = (By.XPATH, f"//ul[@class='variant-option-list flex justify-start gap-05 flex-wrap']//a[text()='{productColor}']")

        self.driver.find_element(*self.color_option).click()
        time.sleep(2)

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()
        time.sleep(2)

    def continue_shopping_products(self):
        self.driver.find_element(*self.continue_shopping_link).click()
        time.sleep(2)

    def back_to_shopping_page(self, selectedGender):
        self.breacrumb_gender_link = (By.CSS_SELECTOR, f".text-interactive[href='/{selectedGender}']")

        self.driver.find_element(self.breacrumb_gender_link).click()
        time.sleep(2)

    def return_to_shopping_page(self, selectedGender):
        self.shop_link = (By.CSS_SELECTOR, f"a.nav-link[href='/{selectedGender}']")
        self.driver.find_element(*self.shop_link).click()
        time.sleep(5)

    def get_products_lists_summary(self, selectedProductList):

        product_summary = []

        for product in selectedProductList:
            product['Total_Product'] = "${:,.2f}".format(product['Total_Product'])
            del product['Sale_Price']
            product_summary.append(product)

        return product_summary















