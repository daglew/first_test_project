from selenium.webdriver.common.by import By

from tests.commons.emails import Email
from tests.commons.pages.automation_practice_create_an_account import Ids as automation_create_an_account_id, \
    dropdown_years, dropdown_day, dropdown_months, state_selector, country_selector
from tests.commons.pages.automation_practice_create_an_account import Xpath as automation_create_an_account_xpath
from tests.objects.pages.automation_practice_find_my_account import AutomationPraticeFindMyAccount


class AutomationPraticeCreateAccount:
    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation"
        self.title = "Login - My Store"

    def open_page(self):
        self.driver.get(self.page)
        title = self.driver.title
        assert self.title == title, f"Expected title: {self.title} is different than current title: {title}."

    def find_element(self, locator: str):
        if locator.startswith("//"):
            element = self.driver.find_element(By.XPATH, locator)
        else:
            element = self.driver.find_element(By.ID, locator)
        return element

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
        return element

    def fulfill_formula(self, title: str, first_name: str, last_name: str, email, password: str, number_day: int,
                        number_months: int, number_years: int, address: str, city: str, state: str, zip_code: str,
                        information: str, selector_country: str, home_number: str, mobile_phone: str,
                        receive_special_offers: bool=True, sign_up_newsletter: bool=True):

        if title.lower() == "mrs":
            self.find_and_click(locator=automation_create_an_account_id.TITLE_MRS_ID)
        elif title.lower() == "mr":
            self.find_and_click(locator=automation_create_an_account_id.TITLE_MR_ID)
        else:
            raise Exception(f"Wrong value: {title}, should be mrs or mr.")

        self.find_input_send_keys(locator=automation_create_an_account_id.FIRST_NAME_INPUT_ID, input_keys=first_name.capitalize())

        self.find_input_send_keys(locator=automation_create_an_account_id.LAST_NAME_INPUT_ID, input_keys=last_name.capitalize())

        self.find_input_send_keys(locator=automation_create_an_account_id.INPUT_EMAIL_ID, input_keys=email)

        self.find_input_send_keys(locator=automation_create_an_account_id.INPUT_PASSWORD_ID, input_keys=password)

        if 1 <= number_day <= 31:
            self.find_and_click(locator=dropdown_day(value=number_day))
        else:
            raise Exception(f"Day number: {number_day} is not between 1-31.")

        if 1 <= number_months <= 12:
            self.find_and_click(locator=dropdown_months(value=number_months))
        else:
            raise Exception(f"Month number: {number_months} is not between 1-12.")

        if 1900 <= number_years <= 2022:
            self.find_and_click(locator=dropdown_years(value=number_years))
        else:
            raise Exception(f"Year number: {number_years} is not between 1900-2022.")

        if sign_up_newsletter:
            self.find_and_click(locator=automation_create_an_account_id.CHECKBOX_NEWSLETTER)

        if receive_special_offers:
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

        self.find_and_click(locator=automation_create_an_account_id.COUNTRY_SELECTOR_ID)

        self.find_input_send_keys(locator=automation_create_an_account_id.ADDITIONAL_INFORMATION_ID, input_keys=information)

        self.find_input_send_keys(locator=automation_create_an_account_id.HOME_PHONE_NUMBER, input_keys=home_number)

        if selector_country == "United States":
            self.find_and_click(locator=country_selector(country=selector_country))
        else:
            raise Exception(f"Country: {selector_country} is not equal 'United States'.")

        if len(mobile_phone) == 9:
            self.find_input_send_keys(locator=automation_create_an_account_id.MOBILE_PHONE_INPUT_ID,
                                      input_keys=mobile_phone)
        else:
            raise Exception(f"Mobile phone: {mobile_phone} is not equal 9 digits.")

        self.find_input_send_keys(locator=automation_create_an_account_id.ADDRRESS_EMAI_INPU,
                                  input_keys=Email.generated_email)

    def click_register_button(self):
        self.find_and_click(locator=automation_create_an_account_id.REGISTER_BUTTON)
        page = AutomationPraticeFindMyAccount(driver=self.driver)
        expected_title = page.title
        title = self.driver.title
        assert expected_title == title, f"Expected title: {expected_title} is different than current title: {title}."
        return page

    def click_sign_out_button(self):
        self.find_and_click(locator=automation_create_an_account_xpath.SIGN_OUT_BUTTON)
        pa


