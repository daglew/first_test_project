from selenium.webdriver.common.by import By
from tests.commons.pages.automation_practice_order_history import Xpath as automation_practice_order_history_xpath
from tests.commons.pages.automation_practice_order_history import Ids as automation_practice_order_history_ids


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

    def click_search_button(self):
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

    def find_printed_summer_dress(self):
        self.find_input_send_keys(locator=automation_practice_order_history_ids.INPUT_SEARCH,
                                  input_keys="Printed Summer Dress")
        self.find_and_click(locator=automation_practice_order_history_xpath.SEARCH_BUTTON)

    def check_alert_warning_visible(self):
        expected_warning = "//p[@class='alert alert-warning']"
        alert_warning = self.find_element(locator=automation_practice_order_history_xpath.ALERT_WARNING).text
        assert alert_warning == expected_warning, f"Expected warning information on the page: {expected_warning} is " \
                                                  f"not equal to current alert waning {alert_warning} "








