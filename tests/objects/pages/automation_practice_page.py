from selenium.webdriver.common.by import By

from tests.commons.pages.automation_practice import Xpath as automation_xpaths
from tests.objects.pages.automation_practice_my_account_page import AutomationPraticeMyAccountPage


class AutomationPracticePage:
    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com"
        self.title = "My Store"

    def open_page(self):
        self.driver.get(self.page)
        title = self.driver.title
        assert self.title == title, \
            f"Expected title: {self.title} is different than current title: {title}."

    def click_sign_in_button(self):
        self.find_and_click(automation_xpaths.SIGN_IN_BUTTON)
        page = AutomationPraticeMyAccountPage(self.driver)
        page.open_page()
        return page

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

