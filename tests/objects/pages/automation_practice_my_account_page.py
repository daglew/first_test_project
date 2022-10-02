from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from tests.commons.pages.automation_practice_my_account import Ids as automation_my_account_ids
from tests.commons.pages.automation_practice_my_account import Xpath as automation_my_account_xpath
from tests.objects.pages.automation_practice_create_account_page import AutomationPraticeCreateAccount


class AutomationPraticeMyAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
        self.title = "Login - My Store"

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

    def enter_email(self, email):
        self.find_input_send_keys(locator=automation_my_account_ids.INPUT_EMAIL_ADDRESS, input_keys=email)

    def click_create_an_account_button(self):
        self.find_and_click(locator=automation_my_account_xpath.BUTTON_CREATE_AN_ACCOUNT)
        page = AutomationPraticeCreateAccount(driver=self.driver)
        expected_title = page.title
        title = self.driver.title
        assert expected_title == title, f"Expected title: {expected_title} is different than current title: {title}."
        return page

    def find_element(self, locator: str):
        if locator.startswith("//"):
            element = self.driver.find_element(By.XPATH, locator)
        else:
            element = self.driver.find_element(By.ID, locator)
        return element

    def wait_for_element_visible(self, locator):
        wait = WebDriverWait(self.driver, timeout=15)
        if locator.startswith("//"):
            wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        else:
            wait.until(EC.visibility_of_element_located((By.ID, locator)))

    def assert_error_visible(self):
        self.wait_for_element_visible(locator=automation_my_account_ids.ALERT_ERROR)
        element = self.find_element(locator=automation_my_account_ids.ALERT_ERROR)
        text = element.text
        expected_error_text = "An account using this email address has already been registered. Please enter " \
                              "a valid password or request a new one."
        assert expected_error_text == text, f"Expected error text: {expected_error_text} is not equal to" \
                                            f"current error text: {text}."
