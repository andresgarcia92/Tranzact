import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutSummaryPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators

    # Sub total
        self.sub_total_items_textlabel = (By.CSS_SELECTOR, ".checkout-summary-block .summary-row:nth-child(1) > div > div:nth-child(1)")

        self.sub_total_amount_textlabel = (
        By.CSS_SELECTOR, ".checkout-summary-block .summary-row:nth-child(1) > div > div:nth-child(2)")

    # Shipping
        self.shipping_method_textlabel = (
        By.CSS_SELECTOR, ".checkout-summary-block .summary-row:nth-child(2) > div > div:nth-child(1)")

        self.shipping_total_textlabel = (
            By.CSS_SELECTOR, ".checkout-summary-block .summary-row:nth-child(2) > div > div:nth-child(2)")

    # Total
        self.tax_textlabel = (By.CSS_SELECTOR, ".checkout-summary-block .summary-row:nth-child(3) > div > div > div:nth-child(2) > span")

        self.total_amount_textlabel = (By.CSS_SELECTOR, ".checkout-summary-block .summary-row:nth-child(3) > div > div.grand-total-value")

    # Methods

    def get_products_list_details(self):
        self.product_list_table = (By.CSS_SELECTOR, "table.listing.items-table tbody tr")
        listings = self.driver.find_elements(*self.product_list_table)

        product_list = []
        products_lists = []

        for listing in listings:

            product_list = {
              "Product_Name" : listing.find_element(By.CSS_SELECTOR, "span.font-semibold").text,
              "Color" : listing.find_element(By.CSS_SELECTOR, "li:nth-of-type(1) span:last-child").text,
              "Size" : listing.find_element(By.CSS_SELECTOR, "li:nth-of-type(2) span:last-child").text,
              "Quantity": listing.find_element(By.CSS_SELECTOR, "span.qty").text,
              "Total_Product" : listing.find_element(By.CSS_SELECTOR, "td:last-child span").text
            }

            products_lists.append(product_list)

        return products_lists




