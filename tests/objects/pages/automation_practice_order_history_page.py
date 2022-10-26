from selenium.webdriver.common.by import By
from tests.commons.pages.automation_practice_order_history import Xpath as automation_practice_order_history_xpath


class AutomationPracticeOrderHistoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com/index.php?controller=history"
        self.title = "Order history - My Store"

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

    def click_search_button(self, locator):
        self.find_and_click(locator=automation_practice_order_history_xpath.SEARCH_BUTTON)

    def find_element(self, locator: str):
        if locator.startswith("//"):
            element = self.driver.find_element(By.XPATH, locator)
        else:
            element = self.driver.find_element(By.ID, locator)
        return element

    def find_elements(self, locator: str):
        if locator.startswith("//"):
            elements = self.driver.find_elements(By.XPATH, locator)
        else:
            elements = self.driver.find_elements(By.ID, locator)
        return elements

    def find_input_send_keys(self, locator: str, input_keys: str) -> object:
        element = self.find_and_click(locator=locator)
        element.clear()
        element.send_keys(input_keys)
        return element




