from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from tests.commons.pages.automation_practice_search_my_store import Xpath as automation_practice_search_my_story_xpath


class AutomationPracticeSearchMyStore:

    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com/index.php?controller=search&orderby=position&orderway=desc&search_query=Printed+Summer+Dress&submit_search="
        self.title = "Search - My Store"

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

    def hover_element_by_mouse(self, locator):
        action = ActionChains(driver=self.driver)
        element = self.find_element(locator)
        action.move_to_element(element).perform()

    def find_input_send_keys(self, locator: str, input_keys: str) -> object:
        element = self.find_and_click(locator=locator)
        element.clear()
        element.send_keys(input_keys)
        return element

    def confirm_order(self):
        self.find_and_click(locator=automation_practice_search_my_story_xpath.PROCEDER_TO_CHECKOUT_2)
