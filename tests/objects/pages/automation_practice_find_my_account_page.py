from selenium.webdriver.common.by import By

from tests.commons.pages.automation_practice_find_my_account import Xpath as automation_practice_find_my_account_xpath
from tests.objects.pages.automation_practice_order_history_page import AutomationPracticeOrderHistoryPage


class AutomationPracticeFindMyAccount:
    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com/index.php?controller=my-account"
        self.title = "My account - My Store"

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

    def find_element(self, locator: str):
        if locator.startswith("//"):
            element = self.driver.find_element(By.XPATH, locator)
        else:
            element = self.driver.find_element(By.ID, locator)
        return element

    def click_sign_out(self):
        self.find_and_click(locator=automation_practice_find_my_account_xpath.SIGN_OUT_BUTTON)

    def assert_user_log_in(self, name, last_name):
        xpath = f"//span[.='{name} {last_name}']"
        element = self.find_element(locator=xpath)
        assert element, f"Element:{element} is visible."
        assert element.text == f"{name} {last_name}", f"Element:{element.text} is visible."

    def click_my_personal_information(self):
        self.find_and_click(locator=automation_practice_find_my_account_xpath.MY_PERSONAL_INFORMATION_BUTTON)

    def click_order_history_and_details(self):
        self.find_and_click(locator=automation_practice_find_my_account_xpath.ORDER_HISTORY_AND_DETAILS_BUTTON)
        page = AutomationPracticeOrderHistoryPage(driver=self.driver)
        page.open_page()
        return page
