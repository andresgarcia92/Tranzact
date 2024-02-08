from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from ChallengeProject.POM.Pages.homePage import HomePage
from ChallengeProject.POM.Pages.loginPage import LoginPage
from ChallengeProject.POM.Pages.createAccountPage import CreateAccountPage
from ChallengeProject.POM.Pages.myAccountPage import MyAccountPage
from ChallengeProject.POM.Data.userData import User
import HtmlTestRunner

class TestCreateAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_CreateAccount_successful(self):
        driver = self.driver
        home = HomePage(driver)
        login = LoginPage(driver)
        createAccount = CreateAccountPage(driver)
        myAccount = MyAccountPage(driver)

        self.fake = Faker()
        self.user_account = User(
            first_name= self.fake.first_name(),
            last_name= self.fake.last_name(),
            email= self.fake.email(),
            password= self.fake.password(),
            telephone=self.fake.phone_number(),
            address = self.fake.address(),
            city = self.fake.city(),
            country = "United States",
            province = "Alabama",
            postcode = 35005
        )
        fullname = self.user_account.first_name + " " + self.user_account.last_name

        #Arrange
        self.driver.get("https://demo.evershop.io/")
        home.clickOn_login_icon()

        login.clickOn_create_and_account()

        #Action
        #Create new user account
        createAccount.enter_fullname(fullname)
        createAccount.enter_email(self.user_account.email)
        createAccount.enter_password(self.user_account.password)
        createAccount.create_account()

        #Go to Account details
        home.see_my_account()
        expectedFullname = myAccount.get_full_name()
        expectedEmail = myAccount.get_email()

        #Assert
        self.assertEqual(expectedFullname, fullname)
        self.assertEqual(expectedEmail, self.user_account.email)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

# To crate a report, open a terminal and run python3 -m ChallengeProject.POM.Tests.createAccountTest
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='ChallengeProject/POM/Reports'))