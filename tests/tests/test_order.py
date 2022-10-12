import logging
import uuid

from selenium.webdriver import ActionChains

from tests.objects.helpers import create_user
from tests.objects.initialize_webdriver import InitializeWebDriver
from tests.commons.pages.automation_practice_order_history import Xpath as automation_practice_order_history_xpath
from tests.commons.pages.automation_practice_order_history import Ids as automation_practice_order_history_ids
from tests.commons.pages.automation_practice_order_search import Xpath as automation_practice_order_search_xpath
from tests.objects.pages.automation_practice_order_search_page import AutomationPracticeOrderSearch


class TestOrder(InitializeWebDriver):

    """
    1. Create user.
    2. Click Order history and details tab.
    3. Check if alert warning is visible.
    """
    def test_order_history_no_item_ordered(self):
        logging.warning("Open this url  http://automationpractice.com/index.php and maximalize window, check title")
        logging.warning("Click on sign in link.")
        logging.warning("Enter your email address in 'Create an account' section.")
        logging.warning("Click on Create an Account button.")
        logging.warning("Enter your Personal Information, Address and Contact info.")
        logging.warning("Validate that user is created.")
        logging.warning("Create user.")

        uniqe_id = str(uuid.uuid4())
        generated_email = f"kazia{uniqe_id[:5]}@gmail.com"
        expected_warning = "You have not placed any orders."

        page = create_user(driver=self.driver,
                           title="Mrs",
                           name="Basia",
                           last_name="Kasia",
                           email=generated_email,
                           password="xyzbgj45",
                           number_day=4,
                           number_months=7,
                           number_years=2002,
                           address="zielona",
                           city="gdansk",
                           state="alaska",
                           zip_code="00000",
                           information="...",
                           home_number="89765423",
                           selector_country="United States",
                           mobile_phone="123456789",
                           receive_special_offers=True,
                           sign_up_newsletter=True)
        logging.warning("Click Order history and details tab.")
        page.click_order_history_and_details()
        logging.warning("Check if alert warning is visible.")
        alert_warning = page.find_element(locator=automation_practice_order_history_xpath.ALERT_WARNING).text
        assert alert_warning == expected_warning, f"Expected warning information on the page: {expected_warning} is " \
                                                  f"not equal to current alert waning {alert_warning} "

    """
    1. Create user.
    2. Click Order history and details tab.
    3. Check if alert warning is visible.
    4. Find Faded Short Sleeve T-shirts.
    5. Click Add to cart.
    6. Confirm order.
    7. Confirm summary.
    8. Confirm address.
    9. Mark agreement and confirm shipping.
    10. Choose and click payment method.
    11. Confirm order.
    12. Back to orders
    13. Check if new order is visible in order reference column.
    """
    def test_order_history_item_ordered(self):
        logging.warning("Open this url  http://automationpractice.com/index.php and maximalize window, check title")
        logging.warning("Click on sign in link.")
        logging.warning("Enter your email address in 'Create an account' section.")
        logging.warning("Click on Create an Account button.")
        logging.warning("Enter your Personal Information, Address and Contact info.")
        logging.warning("Validate that user is created.")
        logging.warning("Create user.")

        uniqe_id = str(uuid.uuid4())
        generated_email = f"kazia{uniqe_id[:5]}@gmail.com"
        expected_warning = "You have not placed any orders."

        page = create_user(driver=self.driver,
                           title="Mrs",
                           name="Basia",
                           last_name="Kasia",
                           email=generated_email,
                           password="xyzbgj45",
                           number_day=4,
                           number_months=7,
                           number_years=2002,
                           address="zielona",
                           city="gdansk",
                           state="alaska",
                           zip_code="00000",
                           information="...",
                           home_number="89765423",
                           selector_country="United States",
                           mobile_phone="123456789",
                           receive_special_offers=True,
                           sign_up_newsletter=True)

        logging.warning("Click Order history and details tab.")
        page = page.click_order_history_and_details()

        logging.warning("Check if alert warning is visible.")
        alert_warning = page.find_element(locator=automation_practice_order_history_xpath.ALERT_WARNING).text
        assert alert_warning == expected_warning, f"Expected warning information on the page: {expected_warning} is " \
                                                  f"not equal to current alert waning {alert_warning} "

        logging.warning("Find Faded Short Sleeve T-shirts.")
        page = AutomationPracticeOrderSearch(driver=self.driver)
        page.find_input_send_keys(locator=automation_practice_order_history_ids.INPUT_SEARCH, input_keys="Faded Short Sleeve T-shirts")
        page.find_and_click(locator=automation_practice_order_history_xpath.SEARCH_BUTTON)

        logging.warning("Click Add to cart.")
        page.hover_element_by_mouse(locator=automation_practice_order_search_xpath.PICTURE)
        page.find_and_click(locator=automation_practice_order_search_xpath.ADD_TO_CART_BUTTON)
        print()



    """
    1. Create user.
    2. Click Order history and details tab.
    3. Check if alert warning is visible.
    4. Find Faded Short Sleeve T-shirts.
    5. Click Add to cart.
    6. Confirm order.
    7. Find Faded Blouses.
    8. Click Add to cart.
    9. Confirm order.
    10. Confirm summary.
    11. Confirm address.
    12. Mark agreement and confirm shipping.
    13. Choose and click payment method.
    14. Confirm order.
    15. Back to orders
    16. Check if new order is visible in order reference column.

    """
    def test_order_history_few_items_ordered(self):
        pass

    """
    1. Create user.
    2. Click Order history and details tab.
    3. Check if alert warning is visible.
    4. Find Faded Short Sleeve T-shirts.
    5. Click Add to cart.
    6. Confirm order.
    7. Confirm summary.
    8. Confirm address.
    9. Mark agreement and confirm shipping.
    10. Choose and click payment method.
    11. Confirm order.
    12. Back to orders
    13. Check if new order is visible in order reference column.
    14. Find Printed Dress.
    15. Click Add to cart.
    16. Confirm order.
    17. Confirm summary.
    18. Confirm address.
    19. Mark agreement and confirm shipping.
    20. Choose and click payment method.
    21. Confirm order.
    22. Back to orders.
    23. Verify that both orders appear in the order column.
    """

    def test_order_history_few_orders(self):
        pass
