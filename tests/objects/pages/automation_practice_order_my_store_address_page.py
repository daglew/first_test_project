from selenium.webdriver.common.by import By
from tests.commons.pages.automation_practice_order_my_store_address import Ids as automation_practice_order_my_store_address_ids
from tests.commons.pages.automation_practice_order_my_store_address import Xpath as automation_practice_order_my_store_address_xpath


class AutomationPracticeOrderMyStoreAddressPage:

    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com/index.php?controller=order&step=1"
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

    def mark_agreement_and_confirm_shipping(self):
        self.find_and_click(locator=automation_practice_order_my_store_address_ids.TEMS_OF_SERVICE_INPUT)
        self.find_and_click(locator=automation_practice_order_my_store_address_xpath.PROCEDER_CHECKOUT_SHIPPING)
