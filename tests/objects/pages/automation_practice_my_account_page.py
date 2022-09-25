from selenium.webdriver.common.by import By

from tests.commons.emails import Email
from tests.commons.pages.automation_practice_my_account import Ids as automation_my_account_ids
from tests.commons.pages.automation_practice_my_account import Xpath as automation_my_account_xpath
from tests.objects.pages.automation_practice_create_account_page import AutomationPraticeCreateAccount


class AutomationPraticeMyAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
        self.title = "Login - My Store"

    def open_page(self):
        self.driver.get(self.page)
        title = self.driver.title
        assert self.title == title, f"Expected title: {self.title} is different than current title: {title}."

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

    def enter_email_and_create_account(self):
        self.find_input_send_keys(locator=automation_my_account_ids.INPUT_EMAIL_ADDRESS, input_keys=Email.generated_email)

    def click_create_An_account_button(self):
        self.find_and_click(locator=automation_my_account_xpath.BUTTON_CREATE_AN_ACCOUNT)
        page = AutomationPraticeCreateAccount(driver=self.driver)
        expected_title = page.title
        title = self.driver.title
        assert expected_title == title, f"Expected title: {expected_title} is different than current title: {title}."
        return page


    # def enter_email_and_create_account(self):
    #     input_email_address_field = self.driver.find_element(By.ID, automation_my_account_ids.INPUT_EMAIL_ADDRESS)
    #     input_email_address_field.click()
    #     input_email_address_field.clear()
    #     input_email_address_field.

    # button_create_an_account = self.driver.find_element(By.XPATH, automation_my_account_xpath.BUTTON_CREATE_AN_ACCOUNT)
    # button_create_an_account.click()
