from selenium.webdriver.common.by import By


class AutomationPracticeOrderPaymentConfirmMyOrder:

    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com/index.php?fc=module&module=bankwire&controller=payment"
        self.title = "My Store"

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
