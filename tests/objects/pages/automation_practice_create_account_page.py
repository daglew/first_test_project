from selenium.webdriver.common.by import By

from tests.commons.pages.automation_practice_my_account import Ids as automation_create_an_account_id


class AutomationPraticeCreateAccount:
    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation"
        self.title = "Login - My Store"

    def open_page(self):
        self.driver.get(self.page)
        title = self.driver.title
        assert self.title == title, f"Expected title: {self.title} is different than current title: {title}."
