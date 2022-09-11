from tests.objects.initialize_webdriver import InitializeWebDriver


class AutomationPracticePage(InitializeWebDriver):
    def __init__(self):
        super(InitializeWebDriver, self).__init__()
        self.page = "http://automationpractice.com/index.php"
        self.title = "Login - My Store"

    def open_page(self):
        self.driver.get(self.page)
        title = self.driver.title
        assert self.title == title, f"Expected title: {self.title} is different than current title: {title}."
