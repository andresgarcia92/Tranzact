import random
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from ChallengeProject.POM.Pages.homePage import HomePage
from ChallengeProject.POM.Pages.createAccountPage import CreateAccountPage
from ChallengeProject.POM.Pages.loginPage import LoginPage
from ChallengeProject.POM.Pages.shopPage import ShopPage
from ChallengeProject.POM.Pages.productDetailPage import ProductDetailPage
from ChallengeProject.POM.Pages.checkoutPage import CheckoutPage
from ChallengeProject.POM.Pages.checkoutSuccessPage import CheckoutSuccessPage
from ChallengeProject.POM.Pages.checkoutSummaryPage import CheckoutSummaryPage
from ChallengeProject.POM.Data.userData import User
from ChallengeProject.POM.Data.productsData import Products
import HtmlTestRunner

class TestPlaceOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_placeOrder_successful(self):
        driver = self.driver
        self.fake = Faker()
        home = HomePage(driver)
        createAccount = CreateAccountPage(driver)
        login = LoginPage(driver)
        shop = ShopPage(driver)
        productDetail = ProductDetailPage(driver)
        checkout = CheckoutPage(driver)
        checkoutSummary = CheckoutSummaryPage(driver)
        checkoutSuccess = CheckoutSuccessPage(driver)
        products = Products(driver)

        selectedGender = random.choice(["women", "men"])
        genderProductsList  = products.getProducts(selectedGender)
        itemsQuantity = 3 #According to this challenge, only 3 items should be bought
        selectedProductList = random.sample(genderProductsList, itemsQuantity)

        # Arrange
        # Generate data for a new user account
        self.fake = Faker()
        self.user_account = User(
            first_name=self.fake.first_name(),
            last_name=self.fake.last_name(),
            email=self.fake.email(),
            password=self.fake.password(),
            telephone=self.fake.phone_number(),
            address=self.fake.address(),
            city=self.fake.city(),
            country="United States",
            province="Alabama",
            postcode=35005

        )
        fullname = self.user_account.first_name + " " + self.user_account.last_name

        # Create an user account
        self.driver.get("https://demo.evershop.io/")
        home.clickOn_login_icon()
        login.clickOn_create_and_account()
        createAccount.enter_fullname(fullname)
        createAccount.enter_email(self.user_account.email)
        createAccount.enter_password(self.user_account.password)
        createAccount.create_account()

        # Actions

        # Select products
        home.go_to_shopping_page(selectedGender)

        #Add selected products to the shop cart
        checkoutProduct = []
        checkoutProducts = []

        for product in selectedProductList:

            checkoutProduct = {
                "Product_Name": product["Product_Name"],
                "Size": random.choice(product["Size"]),
                "Color": random.choice(product["Color"]),
                "Sale_Price": product["Sale_Price"]
            }

            shop.click_On_Product(selectedGender, product["Product_Name"])

            quantity = productDetail.enter_quantity()
            totalProduct = product["Sale_Price"] * int(quantity)

            checkoutProduct["Quantity"] = quantity
            checkoutProduct["Total_Product"] = totalProduct

            checkoutProducts.append(checkoutProduct)

            productDetail.select_size(checkoutProduct["Size"])
            productDetail.select_color(checkoutProduct["Color"])

            productDetail.add_to_cart()
            productDetail.continue_shopping_products()
            productDetail.return_to_shopping_page(selectedGender)

        sum_totalAmount_checkOutProducts = 0
        sum_totalQuantity_checkOutProducts = 0

        for checkoutProduct in checkoutProducts:
            sum_totalAmount_checkOutProducts += checkoutProduct["Total_Product"]
            sum_totalQuantity_checkOutProducts += int(checkoutProduct["Quantity"])

        totalQuantity = sum_totalQuantity_checkOutProducts
        totalAmount = sum_totalAmount_checkOutProducts
        product_list_summary = productDetail.get_products_lists_summary(checkoutProducts)

        # See Order Summary
        shop.see_shop_chart()

        # Go to checkout
        checkout.click_checkout_button()
        checkout.fill_shipping_address(self.user_account)

        shippingMethod = checkout.select_shipping_method()
        totalshipping = checkout.add_shipping_method(shippingMethod)

        # Go to Payment and place order
        checkout.click_continue_payment()
        checkout.select_payment_method()
        totalorder = totalAmount + totalshipping
        checkout.click_place_order()

        # Check order details
        # Order Information
        # Header
        assert "Order #" in self.driver.find_element(*checkoutSuccess.order_number_textlabel).text
        assert f"Thank you {fullname}!" in self.driver.find_element(*checkoutSuccess.client_fullname_textlabel).text

        # Contact Information
        assert fullname == self.driver.find_element(*checkoutSuccess.contact_information_fullname_textlabel).text
        assert self.user_account.email == self.driver.find_element(*checkoutSuccess.contact_information_email_textlabel).text

        # Payment Method
        assert "Credit Card" == self.driver.find_element(*checkoutSuccess.payment_method_textlabel).text

        # Shipping Address
        assert fullname == self.driver.find_element(*checkoutSuccess.shipping_address_fullname_textlabel).text
        assert self.user_account.address.replace("\n", "") == self.driver.find_element(*checkoutSuccess.shipping_address_address_textlabel).text.replace("\n", "")
        postcodeCity = str(self.user_account.postcode) + ", " + self.user_account.city
        assert postcodeCity == self.driver.find_element(*checkoutSuccess.shipping_address_postcode_city_textlabel).text
        assert self.user_account.province == self.driver.find_element(*checkoutSuccess.shipping_address_province_textlabel).text.replace(",", "")
        assert self.user_account.country == self.driver.find_element(*checkoutSuccess.shipping_address_country_textlabel).text
        assert self.user_account.telephone == self.driver.find_element(*checkoutSuccess.shipping_address_telephone_textlabel).text

        # Checkout Summary
        # Products list
        checkout_product_list = checkoutSummary.get_products_list_details()
        #self.assertCountEqual(checkout_product_list, product_list_summary)

        # Sub total
        assert f"{str(itemsQuantity)} items" == self.driver.find_element(*checkoutSummary.sub_total_items_textlabel).text
        assert "${:,.2f}".format(totalAmount) == self.driver.find_element(*checkoutSummary.sub_total_amount_textlabel).text

        # Shipping
        assert shippingMethod == self.driver.find_element(*checkoutSummary.shipping_method_textlabel).text
        assert "${:,.2f}".format(totalshipping) == self.driver.find_element(*checkoutSummary.shipping_total_textlabel).text

        # Total Order
        assert "${:,.2f}".format(totalorder) == self.driver.find_element(*checkoutSummary.total_amount_textlabel).text

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

#  To crate a report, open a terminal and run python3 -m ChallengeProject.POM.Tests.placeOrderTest
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='ChallengeProject/POM/Reports'))




