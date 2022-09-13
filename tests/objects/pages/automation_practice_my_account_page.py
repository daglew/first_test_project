from selenium.webdriver.common.by import By

from tests.commons.pages.automation_practice_my_account import Ids as automation_my_account_ids


class AutomationPraticeMyAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
        self.title = "Login - My Store"

    def open_page(self):
        self.driver.get(self.page)
        title = self.driver.title
        assert self.title == title, f"Expected title: {self.title} is different than current title: {title}."

    # def enter_email_and_create_account(self):
    #     input_email_address_field = self.driver.find_element(By.ID, automation_my_account_ids.INPUT_EMAIL_ADDRESS)
    #     input_email_address_field.click()
    #     input_email_address_field.clear()
    #     input_email_address_field.


