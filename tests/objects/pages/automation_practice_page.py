
class AutomationPracticePage:
    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com"
        self.title = "My Store"

    def open_page(self):
        self.driver.get(self.page)
        title = self.driver.title
        assert self.title == title, f"Expected title: {self.title} is different than current title: {title}."

    def click_sign_in_button(self):
        pass


