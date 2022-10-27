from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from tests.commons.pages.automation_practice_order_search_blouses_add import Xpath as automation_practice_order_search_blouses_add_xpath


class AutomationPracticeSearchBlouses:
    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com/index.php?controller=search&orderby=position&orderway=desc&search_query=Blouses&submit_search="
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

    def confirm_order_blouse(self):
        self.find_and_click(locator=automation_practice_order_search_blouses_add_xpath.ADD_BLOUSE_BUTTON)
        self.find_and_click(locator=automation_practice_order_search_blouses_add_xpath.PROCEED_TO_CHECKOUT_2)




