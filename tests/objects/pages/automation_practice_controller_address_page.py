from selenium.webdriver.common.by import By


class AutomationPraticeControllerAddressPage:
    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com/index.php?controller=identity"
        self.title = "Identity - My Store"

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

    def find_and_take_attribute(self, locator: str):
        if locator.startswith("//"):
            element = self.driver.find_element(By.XPATH, locator)
            element_attribute_value = element.get_attribute("value")
        else:
            element = self.driver.find_element(By.ID, locator)
            element_attribute_value = element.get_attribute("value")
        return element_attribute_value

