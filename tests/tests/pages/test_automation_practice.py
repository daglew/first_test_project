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

    def create_user(self, title, name, last_name, email, password, number_day, number_months, number_years, address,
                    city, state, zip_code, information, home_number, selector_country, mobile_phone,
                    receive_special_offers=True, sign_up_newsletter=True):
        page = AutomationPracticePage(self.driver)
        page.open_page()
        page = page.click_sign_in_button()
        page.enter_email_and_create_account()
        page = page.click_create_An_account_button()
        name = name
        last_name = last_name
        page.fulfill_formula(title=title,
                             first_name=name,
                             last_name=last_name,
                             email=email,
                             password=password,
                             number_day=number_day,
                             number_months=number_months,
                             number_years=number_years,
                             address=address,
                             city=city,
                             state=state,
                             zip_code=zip_code,
                             information=information,
                             home_number=home_number,
                             selector_country=selector_country,
                             mobile_phone=mobile_phone,
                             receive_special_offers=receive_special_offers,
                             sign_up_newsletter=sign_up_newsletter)
        page = page.click_register_button()
        xpath = f"//span[.='{name} {last_name}']"
        element = page.find_element(locator=xpath)
        assert element, f"Element:{element} is visible."
        assert element.text == f"{name} {last_name}", f"Element:{element.text} is visible."
        return page

        # wrong_xpath = f"//span[.='{name} {last_name}+++++']"
        # wrong_element = page.find_element(locator=wrong_xpath)
        # assert wrong_element, f"Element:{wrong_element} is not visible."


    def test_create_account(self):
        logging.warning("Open this url  http://automationpractice.com/index.php and maximalize window, check title")
        logging.warning("Click on sign in link.")
        logging.warning("Enter your email address in 'Create an account' section.")
        logging.warning("Click on Create an Account button.")
        logging.warning("Enter your Personal Information, Address and Contact info.")
        logging.warning("Validate that user is created.")
        self.create_user(title="Mrs",
                         name="Basia",
                         last_name="Kasia",
                         email=Email.generated_email,
                         password="xyzbgj45",
                         number_day="4",
                         number_months="7",
                         number_years="2002",
                         address="zielona",
                         city= "gdansk",
                         state="alaska",
                         zip_code="00000",
                         information="...",
                         home_number="89765423",
                         selector_country="United States",
                         mobile_phone="123456789",
                         receive_special_offers=True,
                         sign_up_newsletter=True)
        print()


    """
    Steps to Automate:
    1. Open this url  http://automationpractice.com/index.php and maximalize window, check title
    2. Click on sign in link.
    3. Enter your email address in 'Create an account' section.
    4. Click on Create an Account button.
    5. Enter your Personal Information, Address and Contact info.
    6. Click on Register button.
    7. Validate that user is created.
    8. Log out user.
    9. Open the page again http://automationpractice.com/index.php?controller=authentication&back=my-account
    11. Enter your email address in 'Create an account' section.
    12. Click on Create an Account button.
    13. Check if error is visible.
    
    """

    def test_create_account_the_same_email(self):
        logging.warning("Open this url  http://automationpractice.com/index.php and maximalize window, check title")
        logging.warning("Click on sign in link.")
        logging.warning("Enter your email address in 'Create an account' section.")
        logging.warning("Click on Create an Account button.")
        logging.warning("Enter your Personal Information, Address and Contact info.")
        logging.warning("Validate that user is created.")
        self.create_user(title="Mrs",
                         name="Basia",
                         last_name="Kasia",
                         email=Email.generated_email,
                         password="xyzbgj45",
                         number_day="4",
                         number_months="7",
                         number_years="2002",
                         address="zielona",
                         city="gdansk",
                         state="alaska",
                         zip_code="00000",
                         information="...",
                         home_number="89765423",
                         selector_country="United States",
                         mobile_phone="123456789",
                         receive_special_offers=True,
                         sign_up_newsletter=True)

        logging.warning("Log out user.")

        logging.warning("Open the page again http://automationpractice.com/index.php?controller=authentication&back=my-account")
        logging.warning("Enter your email address in 'Create an account' section.")
        logging.warning("Click on Create an Account button.")
        logging.warning("Check if error is visible.")


