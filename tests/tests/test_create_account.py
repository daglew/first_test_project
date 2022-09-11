"""
1. Test Case - Automate User Registration process of e-commerce website.
Steps to Automate:
1. Open this url  http://automationpractice.com/index.php and maximalize window
2. Click on sign in link.
3. Enter your email address in 'Create an account' section.
4. Click on Create an Account button.
5. Enter your Personal Information, Address and Contact info.
6. Click on Register button.
7. Validate that user is created.

"""
from time import sleep

from tests.objects.pages.automation_practice_page import AutomationPracticePage


class TestClassOne:

    def test_create_account(self):
        page = AutomationPracticePage()
        page.open_page()
        sleep(5)

