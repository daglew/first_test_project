from selenium.webdriver.common.by import By


class AutomationPracticeOrderPaymentBackToOrders:

    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com/index.php?controller=order-confirmation&id_cart=5103918&id_module=3&id_order=482002&key=8780e63145d4508cdb2a64b5210f8586"
        self.title = "Order confirmation - My Store"

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
