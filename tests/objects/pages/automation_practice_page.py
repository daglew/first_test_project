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
        sign_in_button = self.driver.find_element(By.XPATH, automation_xpaths.SIGN_IN_BUTTON)
        sign_in_button.click()
        page = AutomationPraticeMyAccountPage(self.driver)
        expected_title = page.title
        current_title = self.driver.title
        assert expected_title == current_title, \
            f"Expected_title: {expected_title} is not equal to current_title: {current_title}."
        return page


