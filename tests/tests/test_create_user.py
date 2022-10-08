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
from tests.objects.helpers import create_user
from tests.objects.initialize_webdriver import InitializeWebDriver
from tests.objects.pages.automation_practice_controller_address_page import AutomationPraticeControllerAddressPage
from tests.objects.pages.automation_practice_my_account_page import AutomationPraticeMyAccountPage
from tests.commons.pages.automation_practice_my_account import Xpath as automation_my_account_xpath
from tests.commons.pages.automation_practice_controller_address_account import \
    Ids as automation_practice_controlles_address_ids, day_xpath, month_xpath, year_xpath
from tests.commons.pages.automation_practice_controller_address_account import Xpath as automation_practice_controlles_address_xpath


class TestCreateUser(InitializeWebDriver):

    def test_create_account(self):
        logging.warning("Open this url  http://automationpractice.com/index.php and maximalize window, check title")
        logging.warning("Click on sign in link.")
        logging.warning("Enter your email address in 'Create an account' section.")
        logging.warning("Click on Create an Account button.")
        logging.warning("Enter your Personal Information, Address and Contact info.")
        logging.warning("Validate that user is created.")
        create_user(driver=self.driver,
                    title="Mrs",
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

        page = create_user(driver=self.driver,
                           title="Mrs",
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
        last_name = "Kasia"
        day = 4
        month = 7
        year = 2002
        password = "xyzbgj45"
        radio_button_title = "Mrs"
        page = create_user(driver=self.driver,
                           title=radio_button_title,
                           name=name,
                           last_name=last_name,
                           email=generated_email,
                           password=password,
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

        elements = page.find_elements("//label[@class='top']")
        mrs_element = None
        for element in elements:
            if radio_button_title in element.text:
                mrs_element = element
            else:
                mrs_element = None

        checked_mrs_radio_button = mrs_element.find_element_by_tag_name("span").get_attribute("class")
        assert checked_mrs_radio_button == "checked", f"Expected result is: 'checked' button, " \
                                                     f"current result is: {checked_mrs_radio_button}."

        personal_last_name_attribute = page.find_and_take_attribute(locator=automation_practice_controlles_address_ids.LAST_NAME, attribute="value")
        assert personal_last_name_attribute.rstrip() == last_name, f"Expected personal last name attribute:{last_name}" \
                                                         f"is not equal to current personal last name attribute:{personal_last_name_attribute}."

        personal_day_text = page.find_element(locator=day_xpath(day=day)).text
        assert int(personal_day_text) == day, f"Expected day: {day} is not equal to current personal day: {personal_day_text}."

        personal_month_text = page.find_element(locator=month_xpath(months=month)).text
        assert personal_month_text.rstrip() == "July", f"Expected month: 'July' is not equal to current personal month: {personal_month_text}."

        personal_year_text = page.find_element(locator=year_xpath(years=year)).text
        assert int(personal_year_text) == year, f"Expected year: {year} is not equal to current personal year: {personal_year_text}."

        page.find_input_send_keys(locator=automation_practice_controlles_address_ids.CURRENT_PASSWORD, input_keys=password)

        page.find_and_click(locator=automation_practice_controlles_address_xpath.SAVE_BUTTON)
