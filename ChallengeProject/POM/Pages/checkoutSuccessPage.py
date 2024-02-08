import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutSuccessPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators

    # Order number header
        self.order_number_textlabel = (By.CSS_SELECTOR, "#app  main.content .page-width:nth-child(2) > div:nth-child(1) .thank-you > div > span")
        self.client_fullname_textlabel = (By.CSS_SELECTOR, "#app  main.content .page-width:nth-child(2) > div:nth-child(1) .thank-you > div > div")

    # Customer info
        self.contact_information_fullname_textlabel = (By.CSS_SELECTOR, "div.customer-info div:nth-child(1) > div.mb-2 > div:nth-child(2)")

        self.contact_information_email_textlabel = (By.CSS_SELECTOR, "div.customer-info div:nth-child(1) > div.mb-2 > div:nth-child(3)")

    # Payment method
        self.payment_method_textlabel = (By.CSS_SELECTOR, "div.customer-info div:nth-child(2) > div.mb-2 > div:nth-child(2)")

    # Shipping Address
        self.shipping_address_fullname_textlabel = (By.CSS_SELECTOR, "div:nth-child(1) > div:nth-child(2) > div.text-textSubdued > div > div.full-name")
        self.shipping_address_address_textlabel = (By.CSS_SELECTOR, "div:nth-child(1) > div:nth-child(2) > div.text-textSubdued > div > div.address-one")
        self.shipping_address_postcode_city_textlabel = (By.CSS_SELECTOR, "div:nth-child(1) > div:nth-child(2) > div.text-textSubdued > div > div.city-province-postcode > div:nth-child(1)")
        self.shipping_address_province_textlabel = (By.CSS_SELECTOR, "div:nth-child(1) > div:nth-child(2) > div.text-textSubdued > div > div.city-province-postcode > div:nth-child(2) > span:nth-child(1)")
        self.shipping_address_country_textlabel = (By.CSS_SELECTOR, "div:nth-child(1) > div:nth-child(2) > div.text-textSubdued > div > div.city-province-postcode > div:nth-child(2) > span:nth-child(2)")
        self.shipping_address_telephone_textlabel = (By.CSS_SELECTOR,"div:nth-child(1) > div:nth-child(2) > div.text-textSubdued > div > div.telephone")

    # Billing Address
        self.billing_address_fullname_textlabel = (By.CSS_SELECTOR, "div:nth-child(2) > div:nth-child(2) > div.text-textSubdued > div > div.full-name")
        self.billing_address_address_textlabel = (By.CSS_SELECTOR, "div:nth-child(2) > div:nth-child(2) > div.text-textSubdued > div > div.address-one")
        self.billing_address_province_textlabel = (By.CSS_SELECTOR, "div:nth-child(2) > div:nth-child(2) > div.text-textSubdued > div > div.city-province-postcode > div:nth-child(1)")
        self.billing_address_city_textlabel = (By.CSS_SELECTOR, "div:nth-child(2) > div:nth-child(2) > div.text-textSubdued > div > div.city-province-postcode > div:nth-child(2) > span:nth-child(1)")
        self.billing_address_country_textlabel = (By.CSS_SELECTOR, "div:nth-child(2) > div:nth-child(2) > div.text-textSubdued > div > div.city-province-postcode > div:nth-child(2) > span:nth-child(2)")
        self.billing_address_telephone_textlabel = (By.CSS_SELECTOR, "div:nth-child(2) > div:nth-child(2) > div.text-textSubdued > div > div.telephone")


    #Methods





