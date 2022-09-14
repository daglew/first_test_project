"""
Test Case - Automate User Registration process of e-commerce website.

Steps to Automate:
1. Open this url  http://automationpractice.com/index.php and maximalize window, check title
2. Click on sign in link.
3. Enter your email address in 'Create an account' section.
4. Click on Create an Account button.
5. Enter your Personal Information, Address and Contact info.
6. Click on Register button.
7. Validate that user is created.
"""
import logging

from time import sleep

from selenium.webdriver.common.by import By

from tests.commons.pages.automation_practice import Xpath as automation_xpaths
from tests.objects.initialize_webdriver import InitializeWebDriver
from tests.objects.pages.automation_practice_create_account_page import AutomationPraticeCreateAccount
from tests.objects.pages.automation_practice_my_account_page import AutomationPraticeMyAccountPage
from tests.objects.pages.automation_practice_page import AutomationPracticePage
from tests.commons.pages.automation_practice_my_account import Ids as automation_my_account_ids
from tests.commons.pages.automation_practice_my_account import Xpath as automation_my_account_xpath
from tests.commons.pages.automation_practice_create_an_account import Ids as automation_create_an_account_id



class TestAutomationPractice(InitializeWebDriver):

    def test_create_account(self):
        logging.warning("Open this url  http://automationpractice.com/index.php and maximalize window, check title")
        page = AutomationPracticePage(self.driver)
        page.open_page()

        logging.warning("Click on sign in link.")
        page = page.click_sign_in_button()

        logging.warning("Enter your email address in 'Create an account' section.")
        # page.enter_email_and_create_account()
        input_email_address_field = self.driver.find_element(By.ID, automation_my_account_ids.INPUT_EMAIL_ADDRESS)
        input_email_address_field.click()
        input_email_address_field.clear()
        input_email_address_field.send_keys("zuzia_14@wp.pl")

        logging.warning("Click on Create an Account button.")
        button_create_an_account = self.driver.find_element(By.XPATH, automation_my_account_xpath.BUTTON_CREATE_AN_ACCOUNT)
        button_create_an_account.click()
        page = AutomationPraticeCreateAccount(driver=self.driver)
        expected_title = page.title
        title = self.driver.title

        logging.warning("Enter your Personal Information, Address and Contact info.")
        radio_button_enter_personal_information = self.driver.find_element(By.ID, automation_create_an_account_id.RADIO_BUTTON_PERSONAL_INF)
        radio_button_enter_personal_information.click()




        logging.warning("Click on Register button.")
        logging.warning("Validate that user is created.")


        sleep(5)

