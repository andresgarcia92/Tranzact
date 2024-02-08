import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
        self.checkout_button = (By.CSS_SELECTOR, ".button.primary[href='/checkout']")

        self.fullname_textbox = (By.CSS_SELECTOR, "input[name='address[full_name]']")
        self.telephone_textbox = (By.CSS_SELECTOR, "input[name='address[telephone]']")
        self.address_textbox = (By.CSS_SELECTOR, "input[name='address[address_1]']")
        self.city_textbox = (By.CSS_SELECTOR, "input[name='address[city]']")
        self.country_combobox = (By.CSS_SELECTOR, '#address\[country\]')
        self.province_combobox = (By.CSS_SELECTOR, '#address\[province\]')
        self.postcode_textbox = (By.CSS_SELECTOR, "input[name='address[postcode]']")
        self.shipping_standard_radioButton = (By.XPATH, "//*[@id='checkoutShippingAddressForm']/div[1]/div[6]/div/div/div/div[1]/label/span[1]")
        self.shipping_express_radioButton = (By.XPATH, "//*[@id='checkoutShippingAddressForm']/div[1]/div[6]/div/div/div/div[2]/label/span[1]")

        self.continue_to_payment_button = (By.CSS_SELECTOR, "button.button.primary")

        self.visa_mastercard_radioButton = (By.XPATH, "//*[@id='checkoutPaymentForm']/div[3]/div[3]/div/div/div/div[1]/a")

    #Payment Method
        self.card_element_section = (By.CSS_SELECTOR, "#card-element")
        self.card_number_textbox = (By.CSS_SELECTOR, "input[name='cardnumber'][aria-label='Número de la tarjeta de crédito o débito']")
        self.expiration_date_textbox = (By.CSS_SELECTOR, "input[name='exp-date']")
        self.cvc_textbox = (By.CSS_SELECTOR, "input[name='cvc']")

        #self.place_order_button = (By.CSS_SELECTOR, "button.button.primary")
        self.place_order_button = (By.CSS_SELECTOR, "#app main.content #checkoutPaymentForm div.form-submit-button button.button.primary")



    #Methods
    def click_checkout_button(self):
        self.driver.find_element(*self.checkout_button).click()
        time.sleep(2)

    def fill_shipping_address(self, user):

        self.driver.find_element(*self.fullname_textbox).send_keys(user.first_name + " " + user.last_name)
        self.driver.find_element(*self.telephone_textbox).send_keys(user.telephone)
        self.driver.find_element(*self.address_textbox).send_keys(user.address)
        self.driver.find_element(*self.city_textbox).send_keys(user.city)

        self.driver.find_element(*self.country_combobox).click()
        self.country_option = (By.XPATH, f"//select[@id='address[country]']/option[text()='{user.country}']")
        self.driver.find_element(*self.country_option).click()

        self.driver.find_element(*self.province_combobox).click()
        self.province_option = (By.XPATH, f"//select[@id='address[province]']/option[text()='{user.province}']")
        self.driver.find_element(*self.province_option).click()

        self.driver.find_element(*self.postcode_textbox).send_keys(user.postcode)
        time.sleep(2)

    def select_shipping_method(self):
        return random.choice(["Standard Delivery", "Express Delivery"])

    def add_shipping_method(self, shippingMethod):

        if shippingMethod == "Standard Delivery":
            self.driver.find_element(*self.shipping_standard_radioButton).click()
            shippingCost = 5.00

        elif shippingMethod == "Express Delivery":
            self.driver.find_element(*self.shipping_express_radioButton).click()
            shippingCost = 15.00

        else:
            shippingCost = 0

        return shippingCost

    def click_continue_payment(self):
        self.driver.find_element(*self.continue_to_payment_button).click()
        time.sleep(2)

    def select_payment_method(self):
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.visa_mastercard_radioButton))

        time.sleep(2)

        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[name*='__privateStripeFrame']")))

        card_number_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "cardnumber")))
        card_number_input.send_keys("4242 4242 4242 4242")

        expiration_date_input = self.driver.find_element(*self.expiration_date_textbox)
        expiration_date_input.send_keys("0424")

        cvc_input = self.driver.find_element(*self.cvc_textbox)
        cvc_input.send_keys("242")


        self.driver.switch_to.default_content()

        time.sleep(2)

    def click_place_order(self):
        self.driver.find_element(*self.place_order_button).click()
        time.sleep(2)