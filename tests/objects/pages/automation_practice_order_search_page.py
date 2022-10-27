from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from tests.commons.pages.automation_practice_order_search import Xpath as automation_practice_order_search_xpath
from tests.commons.pages.automation_practice_order_search import Ids as automation_practice_order_search_ids


class AutomationPracticeOrderSearch:
    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com/index.php?controller=search&orderby=position&orderway=desc&search_query=&submit_search="
        self.title = "SEARCH"

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

    def click_add_to_cart(self):
        self.hover_element_by_mouse(locator=automation_practice_order_search_xpath.PICTURE)
        self.find_and_click(locator=automation_practice_order_search_xpath.ADD_TO_CART_BUTTON)

    def confirm_order(self):
        self.find_and_click(locator=automation_practice_order_search_xpath.PROCEED_TO_CHECKOUT)

    def find_faded_blouses(self):
        self.find_input_send_keys(locator=automation_practice_order_search_ids.INPUT_SEARCH, input_keys="Blouses")
        self.find_and_click(locator=automation_practice_order_search_xpath.SEARCH_BUTTON)

