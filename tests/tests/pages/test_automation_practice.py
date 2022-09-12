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
from tests.objects.pages.automation_practice_my_account_page import AutomationPraticeMyAccountPage
from tests.objects.pages.automation_practice_page import AutomationPracticePage


class TestAutomationPractice(InitializeWebDriver):

    def test_create_account(self):
        logging.warning("Open this url  http://automationpractice.com/index.php and maximalize window, check title")

        page = AutomationPracticePage(self.driver)
        page.open_page()

        logging.warning("Click on sign in link.")

        sign_in_button = self.driver.find_element(By.XPATH, automation_xpaths.SIGN_IN_BUTTON)
        sign_in_button.click()

        page = AutomationPraticeMyAccountPage(self.driver)
        expected_title = page.title
        current_title = self.driver.title
        assert expected_title == current_title, f"Expected_title: {expected_title} is not equal to current_title: {current_title}."




        logging.warning("Enter your email address in 'Create an account' section.")
        logging.warning("Click on Create an Account button.")
        logging.warning("Enter your Personal Information, Address and Contact info.")
        logging.warning("Click on Register button.")
        logging.warning("Validate that user is created.")


        sleep(5)

