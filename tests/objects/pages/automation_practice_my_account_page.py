class AutomationPraticeMyAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.page = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
        self.title = "Login - My Store"

    def open_page(self):
        self.driver.get(self.page)
        title = self.driver.title
        assert self.title == title, f"Expected title: {self.title} is different than current title: {title}."
