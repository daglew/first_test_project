import unittest

from selenium import webdriver

from tests.objects.paths import Paths


class WebDriverTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.driver.implicitly_wait(time_to_wait=15)

    def tearDown(self):
        self.driver.close()