from selenium.webdriver.common.by import By
from tests.commons.pages.automation_practice_order_my_store import Xpath as automation_practice_order_my_store_xpath
from tests.commons.pages.automation_practice_order_my_my_store_payment_method import Xpath as automation_practice_order_my_my_store_payment_method_xpath, pay_by_check


class AutomationPracticeOrderMyStorePage:

    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com/index.php?controller=order"
        self.title = "Order - My Store"

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

    def confirm_address(self):
        self.find_and_click(locator=automation_practice_order_my_store_xpath.PROCEED_TO_CHECKOUT_BUTTON)


    # def confirm_summary(self):
    #     page = AutomationPracticeOrderMyStorePage(driver=self.driver)
    #     page.open_page()
    #     self.find_and_click(locator=automation_practice_order_my_store_xpath.PROCEED_TO_CHECKOUT_BUTTON)
    #     return page
