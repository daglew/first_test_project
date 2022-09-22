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

from tests.commons.emails import Email
from tests.commons.pages.automation_practice import Xpath as automation_xpaths
from tests.objects.initialize_webdriver import InitializeWebDriver
from tests.objects.pages.automation_practice_create_account_page import AutomationPraticeCreateAccount
from tests.objects.pages.automation_practice_find_my_account import AutomationPraticeFindMyAccount
from tests.objects.pages.automation_practice_my_account_page import AutomationPraticeMyAccountPage
from tests.objects.pages.automation_practice_page import AutomationPracticePage
from tests.commons.pages.automation_practice_my_account import Ids as automation_my_account_ids
from tests.commons.pages.automation_practice_my_account import Xpath as automation_my_account_xpath
from tests.commons.pages.automation_practice_create_an_account import Ids as automation_create_an_account_id, \
    dropdown_years, dropdown_day, dropdown_months, state_selector, country_selector
from tests.commons.pages.automation_practice_find_my_account import Ids as automation_practice_find_my_account



class TestAutomationPractice(InitializeWebDriver):

    def find_and_click(self, locator: str):
        if locator.startswith("//"):
            element = self.driver.find_element(By.XPATH, locator)
            element.click()
        else:
            element = self.driver.find_element(By.ID, locator)
            element.click()
        return element

    def find_input_send_keys(self, locator: str, input_keys: str) -> object:
        element = self.find_and_click(locator=locator)
        element.clear()
        element.send_keys(input_keys)

    def test_create_account(self):
        logging.warning("Open this url  http://automationpractice.com/index.php and maximalize window, check title")
        page = AutomationPracticePage(self.driver)
        page.open_page()

        logging.warning("Click on sign in link.")
        page = page.click_sign_in_button()

        logging.warning("Enter your email address in 'Create an account' section.")
        # page.enter_email_and_create_account()

        self.find_input_send_keys(locator=automation_my_account_ids.INPUT_EMAIL_ADDRESS, input_keys=Email.generated_email)

        logging.warning("Click on Create an Account button.")
        button_create_an_account = self.driver.find_element(By.XPATH, automation_my_account_xpath.BUTTON_CREATE_AN_ACCOUNT)
        button_create_an_account.click()
        page = AutomationPraticeCreateAccount(driver=self.driver)
        expected_title = page.title
        title = self.driver.title
        assert expected_title == title, f"Expected title: {expected_title} is different than current title: {title}."

        logging.warning("Enter your Personal Information, Address and Contact info.")
        self.find_and_click(locator=automation_create_an_account_id.TITLE_MRS_ID)

        self.find_input_send_keys(locator=automation_create_an_account_id.FIRST_NAME_INPUT_ID, input_keys="Kazia")

        self.find_input_send_keys(locator=automation_create_an_account_id.LAST_NAME_INPUT_ID, input_keys="Blanka")

        self.find_input_send_keys(locator=automation_create_an_account_id.INPUT_EMAIL_ID, input_keys=Email.generated_email)

        self.find_input_send_keys(locator=automation_create_an_account_id.INPUT_PASSWORD_ID, input_keys="fortuna217")

        self.find_and_click(locator=dropdown_day(value=3))

        self.find_and_click(locator=dropdown_months(value=2))

        self.find_and_click(locator=dropdown_years(value=2002))

        self.find_and_click(locator=automation_create_an_account_id.CHECKBOX_NEWSLETTER)

        self.find_and_click(locator=automation_create_an_account_id.CHECKBOX_RECEIVE_SPECIAL_OFFERTS)

        self.find_input_send_keys(locator=automation_create_an_account_id.FIRST_NAME_INPUT_ID_2, input_keys="Kazia")

        self.find_input_send_keys(locator=automation_create_an_account_id.LAST_NAME_INPUT_ID_2, input_keys="Blanka")

        self.find_input_send_keys(locator=automation_create_an_account_id.ADDRESS_INPUT, input_keys="292 Browning Lane")

        self.find_input_send_keys(locator=automation_create_an_account_id.CITY_INPUT, input_keys="Juneau")

        self.find_and_click(locator=state_selector(value="Alaska"))

        self.find_input_send_keys(locator=automation_create_an_account_id.ZIP_CODE_INPUT, input_keys="99501")

        self.find_and_click(locator=automation_create_an_account_id.COUNTRY_SELECTOR_ID)

        self.find_and_click(locator=country_selector(country="United States"))

        self.find_input_send_keys(locator=automation_create_an_account_id.MOBILE_PHONE_INPUT_ID, input_keys="123456789")

        self.find_input_send_keys(locator=automation_create_an_account_id.ADDRRESS_EMAI_INPU, input_keys=Email.generated_email)

        logging.warning("Click on Register button.")
        self.find_and_click(locator=automation_create_an_account_id.REGISTER_BUTTON)

    def fulfill_formula(self, title, first_name: str, last_name: str, email, password: str, number_day: int,
                        number_months: int, number_years: int, address: str, city: str, state: str, zip_code: str,
                        information: str):
        if title.lower() == "mrs":
            self.find_and_click(locator=automation_create_an_account_id.TITLE_MRS_ID)
        else:
            self.find_and_click(locator=automation_create_an_account_id.TITLE_MR_ID)

        self.find_input_send_keys(locator=automation_create_an_account_id.FIRST_NAME_INPUT_ID, input_keys=first_name.capitalize())

        self.find_input_send_keys(locator=automation_create_an_account_id.LAST_NAME_INPUT_ID, input_keys=last_name.capitalize())

        self.find_input_send_keys(locator=automation_create_an_account_id.INPUT_EMAIL_ID, input_keys=email.generated_email)

        self.find_input_send_keys(locator=automation_create_an_account_id.INPUT_PASSWORD_ID, input_keys=password)

        if 1 <= number_day <= 31:
            self.find_and_click(locator=dropdown_day(value=number_day))
        else:
            raise Exception(f"Number day: {number_day} is not between 1-31.")

        if 1 <= number_months <= 12:
            self.find_and_click(locator=dropdown_months(value=number_months))
        else:
            raise Exception(f"Number month: {number_months} is not between 1-12.")

        if 1900 <= number_years <= 2022:
            self.find_and_click(locator=dropdown_years(value=number_years))

        else:
            raise Exception(f"Number years: {number_years} is not between 1900-2022.")

        self.find_and_click(locator=automation_create_an_account_id.CHECKBOX_NEWSLETTER)

        self.find_and_click(locator=automation_create_an_account_id.CHECKBOX_RECEIVE_SPECIAL_OFFERTS)

        self.find_input_send_keys(locator=automation_create_an_account_id.FIRST_NAME_INPUT_ID_2, input_keys=first_name.capitalize())

        self.find_input_send_keys(locator=automation_create_an_account_id.LAST_NAME_INPUT_ID_2, input_keys=last_name.capitalize())

        self.find_input_send_keys(locator=automation_create_an_account_id.ADDRESS_INPUT, input_keys=address.capitalize())

        self.find_input_send_keys(locator=automation_create_an_account_id.CITY_INPUT, input_keys=city.capitalize())

        self.find_and_click(locator=state_selector(value=state))

        if len(zip_code) == 5:
            self.find_input_send_keys(locator=automation_create_an_account_id.ZIP_CODE_INPUT, input_keys=zip_code)
        else:
            raise Exception(f"Zip code: {zip_code} is not equal 5 digits.")
            raise Exception(f"Zip code: {zip_code} is not equal 5 digits.")
            raise Exception(f"Zip code: {zip_code} is not equal 5 digits.")




        self.find_and_click(locator=automation_create_an_account_id.COUNTRY_SELECTOR_ID)

        self.find_input_send_keys(locator=automation_create_an_account_id.ADDITIONAL_INFORMATION_ID, input_keys=information)

        self.find_and_click(locator=country_selector(country="United States"))

        self.find_input_send_keys(locator=automation_create_an_account_id.MOBILE_PHONE_INPUT_ID,
                                      input_keys="123456789")

        self.find_input_send_keys(locator=automation_create_an_account_id.ADDRRESS_EMAI_INPU,
                                      input_keys=Email.generated_email)

        logging.warning("Click on Register button.")
        self.find_and_click(locator=automation_create_an_account_id.REGISTER_BUTTON)

        logging.warning("Validate that user is created.")
        writing_my_account = self.driver.find_element(By.ID, automation_practice_find_my_account.PAGE_MY_ACCOUNT)
        writing_my_account.click()
        page = AutomationPraticeFindMyAccount(driver=self.driver)
        expected_title = page.title
        title = self.driver.title
        assert expected_title == title, f"Expected title: {expected_title} is different than current title: {title}."


        sleep(5)

