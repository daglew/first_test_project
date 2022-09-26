from selenium.webdriver.common.by import By

from tests.objects.initialize_webdriver import InitializeWebDriver

def find_and_click(self, element):
    if element.startswith("//"):
        sign_in_button = self.driver.find_element(By.XPATH, element)
    else:
        sign_in_button = self.driver.find_element(By.ID, element)
    sign_in_button.click()