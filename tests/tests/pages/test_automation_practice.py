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

from tests.commons.emails import Email
from tests.objects.initialize_webdriver import InitializeWebDriver
from tests.objects.pages.automation_practice_page import AutomationPracticePage


class TestAutomationPractice(InitializeWebDriver):

    def test_create_account(self):
        logging.warning("Open this url  http://automationpractice.com/index.php and maximalize window, check title")
        page = AutomationPracticePage(self.driver)
        page.open_page()

        logging.warning("Click on sign in link.")
        page = page.click_sign_in_button()

        logging.warning("Enter your email address in 'Create an account' section.")
        page.enter_email_and_create_account()

        logging.warning("Click on Create an Account button.")
        page = page.click_create_An_account_button()

        logging.warning("Enter your Personal Information, Address and Contact info.")
        name = "Kasia"
        last_name = "Basia"
        page.fulfill_formula(title="mrs",
                             first_name=name,
                             last_name=last_name,
                             email=Email.generated_email,
                             password="olga56",
                             number_day=2,
                             number_months=2,
                             number_years=2002,
                             address="blotna",
                             city="Sitka",
                             state="Alaska",
                             zip_code="00000",
                             information="I live in Alaska.",
                             home_number="5678903",
                             selector_country="United States",
                             mobile_phone="123456789",
                             receive_special_offers=True,
                             sign_up_newsletter=True)
        page.click_register_button()

        logging.warning("Validate that user is created.")

        xpath = f"//span[.='{name} {last_name}']"
        element = page.find_element(locator=xpath)
        assert element, f"Element:{element} is visible."
        assert element.text == f"{name} {last_name}", f"Element:{element.text} is visible."

        # wrong_xpath = f"//span[.='{name} {last_name}+++++']"
        # wrong_element = page.find_element(locator=wrong_xpath)
        # assert wrong_element, f"Element:{wrong_element} is not visible."
