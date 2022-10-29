from selenium.webdriver.common.by import By

from tests.commons.pages.automation_practice_order_my_my_store_payment_method import pay_by_check


class AutomationPracticeOrderMyStorePaymentMethod:

    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com/index.php?controller=order&multi-shipping="
        self.title = "Order - My Store"

    def open_page(self, not_getting_page=False):
        if not not_getting_page:
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

    def pay_method(self, check_pay):
        self.find_and_click(locator=pay_by_check(check_pay))

    # def pay_method(self, check_pay):
    #     self.find_and_click(locator=pay_by_check(check_pay))

    # def payment_method2(self, element: str):
    #     if element == "Pay by bank wire":
    #         self.find_and_click(locator=automation_practice_order_my_my_store_payment_method_xpath.PAY_BY_BANK_INPUT)
    #     elif element == "Pay by check":
    #         self.find_and_click(locator=automation_practice_order_my_my_store_payment_method_xpath.PAY_BY_CHECK_INPUT)
    #     else:
    #         raise Exception(f"Wrong value should be 'Pay by bank wire' or 'Pay by check'.")

