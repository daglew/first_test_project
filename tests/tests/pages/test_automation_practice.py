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
import uuid

from tests.commons.emails import Email
from tests.objects.initialize_webdriver import InitializeWebDriver
from tests.objects.pages.automation_practice_controller_address_page import AutomationPraticeControllerAddressPage
from tests.objects.pages.automation_practice_my_account_page import AutomationPraticeMyAccountPage
from tests.objects.pages.automation_practice_page import AutomationPracticePage
from tests.commons.pages.automation_practice_my_account import Xpath as automation_my_account_xpath
from tests.commons.pages.automation_practice_controller_address_account import \
    Ids as automation_practice_controlles_address_ids, day_xpath, month_xpath, year_xpath


class TestAutomationPractice(InitializeWebDriver):

    def create_user(self, title, name, last_name, email, password, number_day, number_months, number_years, address,
                    city, state, zip_code, information, home_number, selector_country, mobile_phone,
                    receive_special_offers=True, sign_up_newsletter=True):
        page = AutomationPracticePage(self.driver)
        page.open_page()
        page = page.click_sign_in_button()
        page.enter_email(email=email)
        page = page.click_create_an_account_button()
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
        page.assert_user_log_in(name=name, last_name=last_name)
        return page

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
                         number_day=4,
                         number_months=7,
                         number_years=2002,
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

        uniqe_id = str(uuid.uuid4())
        generated_email = f"kazia{uniqe_id[:5]}@gmail.com"

        page = self.create_user(title="Mrs",
                                name="Basia",
                                last_name="Kasia",
                                email=generated_email,
                                password="xyzbgj45",
                                number_day=4,
                                number_months=7,
                                number_years=2002,
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
        page.click_sign_out()

        logging.warning("Open the page again http://automationpractice.com/index.php?controller=authentication&back=my-account")
        page = AutomationPraticeMyAccountPage(self.driver)
        page.open_page()

        logging.warning("Enter your email address in 'Create an account' section.")
        page.enter_email(email=generated_email)

        logging.warning("Click on Create an Account button.")
        page.find_and_click(locator=automation_my_account_xpath.BUTTON_CREATE_AN_ACCOUNT)

        logging.warning("Check if error is visible.")
        page.assert_error_visible()


    """
    Steps to Automate:
    1. Open this url  http://automationpractice.com/index.php and maximalize window, check title
    2. Click on sign in link.
    3. Enter your email address in 'Create an account' section.
    4. Click on Create an Account button.
    5. Enter your Personal Information, Address and Contact info.
    6. Click on Register button.
    7. Validate that user is created.
    8. Open my personal information.
    9. Check if user data is correct.
    """

    def test_personal_information_correct(self):
        logging.warning("Open this url  http://automationpractice.com/index.php and maximalize window, check title")
        logging.warning("Click on sign in link.")
        logging.warning("Enter your email address in 'Create an account' section.")
        logging.warning("Click on Create an Account button.")
        logging.warning("Enter your Personal Information, Address and Contact info.")
        logging.warning("Validate that user is created.")

        uniqe_id = str(uuid.uuid4())
        generated_email = f"kazia{uniqe_id[:5]}@gmail.com"
        name = "Basia"
        day = 4
        month = 7
        year = 2002
        page = self.create_user(title="Mrs",
                                name=name,
                                last_name="Kasia",
                                email=generated_email,
                                password="xyzbgj45",
                                number_day=day,
                                number_months=month,
                                number_years=year,
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

        logging.warning("Open my personal information.")
        page.click_my_personal_information()
        page = AutomationPraticeControllerAddressPage(self.driver)
        page.open_page()

        logging.warning("Check if user data is correct.")
        personal_name_attribute = page.find_and_take_attribute(locator=automation_practice_controlles_address_ids.FIRST_NAME, attribute="value")
        assert personal_name_attribute == name, f"Expected personal name attribute: {name} is not equal to current personal"\
                                                f"name attribute: {personal_name_attribute}."

        personal_day_text = page.find_element(locator=day_xpath(day=day)).text
        assert int(personal_day_text) == day, f"Expected day: {day} is not equal to current personal day: {personal_day_text}."

        personal_month_text = page.find_element(locator=month_xpath(months=month)).text
        assert personal_month_text.rstrip() == "July", f"Expected month: 'July' is not equal to current personal month: {personal_month_text}."

        personal_year_text = page.find_element(locator=year_xpath(years=year)).text
        assert int(personal_year_text) == year, f"Expected year: {year} is not equal to current personal year: {personal_year_text}."
print()

