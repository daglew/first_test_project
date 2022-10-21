import logging
import uuid
from datetime import time

from tests.objects.helpers import create_user
from tests.objects.initialize_webdriver import InitializeWebDriver
from tests.commons.pages.automation_practice_order_history import Xpath as automation_practice_order_history_xpath
from tests.commons.pages.automation_practice_order_history import Ids as automation_practice_order_history_ids
from tests.commons.pages.automation_practice_order_search import Xpath as automation_practice_order_search_xpath
from tests.commons.pages.automation_practice_order_search import Ids as automation_practice_order_search_ids
from tests.objects.pages.automation_practice_back_to_order_history_page import AutomationPracticeBackToOrderHistory
from tests.objects.pages.automation_practice_order_casrt_summary_page import AutomationPracticeCartSummary
from tests.objects.pages.automation_practice_order_my_my_store_payment_method_page import \
    AutomationPracticeOrderMyStorePaymentMethod
from tests.objects.pages.automation_practice_order_my_store_address_page import \
    AutomationPracticeOrderMyStoreAddressPage
from tests.objects.pages.automation_practice_order_my_store_page import AutomationPracticeOrderMyStorePage
from tests.objects.pages.automation_practice_order_my_store_shipping_page import \
    AutomationPracticeOrderMyStoreShippingPage
from tests.objects.pages.automation_practice_order_payment_back_to_orders_page import \
    AutomationPracticeOrderPaymentBackToOrders
from tests.objects.pages.automation_practice_order_payment_confirm_my_order_page import \
    AutomationPracticeOrderPaymentConfirmMyOrder
from tests.objects.pages.automation_practice_order_search_blouses_add_page import AutomationPracticeSearchBlouses
from tests.objects.pages.automation_practice_order_search_page import AutomationPracticeOrderSearch
from tests.commons.pages.automation_practice_order_my_store import Xpath as automation_practice_order_my_store_xpath
from tests.commons.pages.automation_practice_order_my_store_address import Xpath as automation_practice_order_my_store_address_xpath
from tests.commons.pages.automation_practice_order_my_store_shipping import Ids as automation_practice_order_my_store_shipping_ids
from tests.commons.pages.automation_practice_order_my_store_shipping import Xpath as automation_practice_order_my_store_shipping_xpath
from tests.commons.pages.automation_practice_order_my_my_store_payment_method import Xpath as automation_practice_order_my_my_store_payment_method_xpath
from tests.commons.pages.automation_practice_order_payment_confirm_my_order import Xpath as automation_practice_order_payment_confirm_my_order_xpath
from tests.commons.pages.automation_practice_order_payment_back_to_orders import Xpath as automation_practice_order_payment_back_to_orders_xpath
from tests.commons.pages.automation_practice_back_to_order_history import Xpath as automation_practice_back_to_order_history_xpath
from tests.commons.pages.automation_practice_order_search_blouses_add import Xpath as automation_practice_order_search_blouses_add_xpath
from tests.commons.pages.automation_practice_order_casrt_summary import Xpath as automation_practice_order_casrt_summary_xpath
from tests.commons.pages.automation_practice_back_to_order_history import Ids as automation_practice_back_to_order_history_ids




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

        logging.warning("Confirm order.")
        page.find_and_click(locator=automation_practice_order_search_xpath.PROCEED_TO_CHECKOUT)

        logging.warning("Confirm summary.")
        page = AutomationPracticeOrderMyStorePage(driver=self.driver)
        page.find_and_click(locator=automation_practice_order_my_store_xpath.PROCEED_TO_CHECKOUT_BUTTON)

        logging.warning("Mark agreement and confirm shipping.")
        page = AutomationPracticeOrderMyStoreAddressPage(driver=self.driver)
        page.find_and_click(locator=automation_practice_order_my_store_address_xpath.PROCEED_TO_CHECKOUT_ADDRESS_BUTTON)

        logging.warning("Choose and click payment method.")
        page = AutomationPracticeOrderMyStoreShippingPage(driver=self.driver)
        page.find_and_click(locator=automation_practice_order_my_store_shipping_ids.TEMS_OF_SERVICE_INPUT)
        page.find_and_click(locator=automation_practice_order_my_store_shipping_xpath.PROCEED_TO_CHECKOUT_SHIPPING_BUTTON)

        logging.warning("Confirm order.")
        page = AutomationPracticeOrderMyStorePaymentMethod(driver=self.driver)
        page.open_page(not_getting_page=True)
        page.find_and_click(locator=automation_practice_order_my_my_store_payment_method_xpath.PAY_BY_BANK_INPUT)

        page = AutomationPracticeOrderPaymentConfirmMyOrder(driver=self.driver)
        page.open_page()
        page.find_and_click(locator=automation_practice_order_payment_confirm_my_order_xpath.I_CONFIRM_MY_ORDER_BUTTON)

        logging.warning("Back to orders")
        page = AutomationPracticeOrderPaymentBackToOrders(driver=self.driver)
        page.open_page(not_getting_page=True)
        page.find_and_click(locator=automation_practice_order_payment_back_to_orders_xpath.BACK_TO_ORDERS)

        logging.warning("Check if new order is visible in order reference column.")
        page = AutomationPracticeBackToOrderHistory(driver=self.driver)
        page.open_page()
        check_reference = page.find_elements(locator=automation_practice_back_to_order_history_xpath.ORDER_REFERENCE)
        assert len(check_reference) == 1, f"Expected result is 1 item list, current result is: {check_reference}."

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
        page.find_input_send_keys(locator=automation_practice_order_search_ids.INPUT_SEARCH,
                                  input_keys="Faded Short Sleeve T-shirts")
        page.find_and_click(locator=automation_practice_order_search_xpath.SEARCH_BUTTON)

        logging.warning("Click Add to cart.")
        page.hover_element_by_mouse(locator=automation_practice_order_search_xpath.PICTURE)
        page.find_and_click(locator=automation_practice_order_search_xpath.ADD_TO_CART_BUTTON)

        logging.warning("Confirm order.")
        page.find_and_click(locator=automation_practice_order_search_xpath.PROCEED_TO_CHECKOUT)

        logging.warning("Find Faded Blouses.")
        page.find_input_send_keys(locator=automation_practice_order_search_ids.INPUT_SEARCH, input_keys="Blouses")
        page.find_and_click(locator=automation_practice_order_search_xpath.SEARCH_BUTTON)

        logging.warning("Click Add to cart.")
        page = AutomationPracticeSearchBlouses(driver=self.driver)
        page.hover_element_by_mouse(locator=automation_practice_order_search_blouses_add_xpath.PICTURE_BLOUSE)

        logging.warning("Confirm order.")
        page.find_and_click(locator=automation_practice_order_search_blouses_add_xpath.ADD_BLOUSE_BUTTON)
        page.find_and_click(locator=automation_practice_order_search_blouses_add_xpath.PROCEED_TO_CHECKOUT_2)

        logging.warning("Confirm summary.")
        page = AutomationPracticeCartSummary(driver=self.driver)
        check_number_product = page.find_elements(locator=automation_practice_order_casrt_summary_xpath.PRODUCT)
        assert len(check_number_product) == 2, f"Expected result is 2 item list, current result is: {check_number_product}."

        logging.warning("Confirm address.")
        page.find_and_click(locator=automation_practice_order_my_store_xpath.PROCEED_TO_CHECKOUT_BUTTON)

        logging.warning("Mark agreement and confirm shipping.")
        page = AutomationPracticeOrderMyStoreAddressPage(driver=self.driver)
        page.find_and_click(locator=automation_practice_order_my_store_address_xpath.PROCEED_TO_CHECKOUT_ADDRESS_BUTTON)

        logging.warning("Choose and click payment method.")
        page = AutomationPracticeOrderMyStoreShippingPage(driver=self.driver)
        page.find_and_click(locator=automation_practice_order_my_store_shipping_ids.TEMS_OF_SERVICE_INPUT)
        page.find_and_click(locator=automation_practice_order_my_store_shipping_xpath.PROCEED_TO_CHECKOUT_SHIPPING_BUTTON)

        logging.warning("Confirm order.")
        page = AutomationPracticeOrderMyStorePaymentMethod(driver=self.driver)
        page.open_page(not_getting_page=True)
        page.find_and_click(locator=automation_practice_order_my_my_store_payment_method_xpath.PAY_BY_BANK_INPUT)
        page.find_and_click(locator=automation_practice_order_payment_confirm_my_order_xpath.I_CONFIRM_MY_ORDER_BUTTON)

        logging.warning("Back to orders")
        page = AutomationPracticeOrderPaymentBackToOrders(driver=self.driver)
        page.open_page(not_getting_page=True)
        page.find_and_click(locator=automation_practice_order_payment_back_to_orders_xpath.BACK_TO_ORDERS)

        logging.warning("Check if new order is visible in order reference column.")
        page = AutomationPracticeBackToOrderHistory(driver=self.driver)
        page.open_page()
        check_reference = page.find_elements(locator=automation_practice_back_to_order_history_xpath.ORDER_REFERENCE)
        assert len(check_reference) == 1, f"Expected result is 1 item list, current result is: {check_reference}."




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
    14. Find Printed Summer Dress.
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
        page.find_input_send_keys(locator=automation_practice_order_history_ids.INPUT_SEARCH,
                                  input_keys="Faded Short Sleeve T-shirts")
        page.find_and_click(locator=automation_practice_order_history_xpath.SEARCH_BUTTON)

        logging.warning("Click Add to cart.")
        page.hover_element_by_mouse(locator=automation_practice_order_search_xpath.PICTURE)
        page.find_and_click(locator=automation_practice_order_search_xpath.ADD_TO_CART_BUTTON)

        logging.warning("Confirm order.")
        page.find_and_click(locator=automation_practice_order_search_xpath.PROCEED_TO_CHECKOUT)

        logging.warning("Confirm summary.")
        page = AutomationPracticeOrderMyStorePage(driver=self.driver)
        page.find_and_click(locator=automation_practice_order_my_store_xpath.PROCEED_TO_CHECKOUT_BUTTON)

        logging.warning("Mark agreement and confirm shipping.")
        page = AutomationPracticeOrderMyStoreAddressPage(driver=self.driver)
        page.find_and_click(locator=automation_practice_order_my_store_address_xpath.PROCEED_TO_CHECKOUT_ADDRESS_BUTTON)

        logging.warning("Choose and click payment method.")
        page = AutomationPracticeOrderMyStoreShippingPage(driver=self.driver)
        page.find_and_click(locator=automation_practice_order_my_store_shipping_ids.TEMS_OF_SERVICE_INPUT)
        page.find_and_click(locator=automation_practice_order_my_store_shipping_xpath.PROCEED_TO_CHECKOUT_SHIPPING_BUTTON)

        logging.warning("Confirm order.")
        page = AutomationPracticeOrderMyStorePaymentMethod(driver=self.driver)
        page.open_page(not_getting_page=True)
        page.find_and_click(locator=automation_practice_order_my_my_store_payment_method_xpath.PAY_BY_BANK_INPUT)

        page = AutomationPracticeOrderPaymentConfirmMyOrder(driver=self.driver)
        page.open_page()
        page.find_and_click(locator=automation_practice_order_payment_confirm_my_order_xpath.I_CONFIRM_MY_ORDER_BUTTON)

        logging.warning("Back to orders")
        page = AutomationPracticeOrderPaymentBackToOrders(driver=self.driver)
        page.open_page(not_getting_page=True)
        page.find_and_click(locator=automation_practice_order_payment_back_to_orders_xpath.BACK_TO_ORDERS)

        logging.warning("Check if new order is visible in order reference column.")
        page = AutomationPracticeBackToOrderHistory(driver=self.driver)
        page.open_page()
        check_reference = page.find_elements(locator=automation_practice_back_to_order_history_xpath.ORDER_REFERENCE)
        assert len(check_reference) == 1, f"Expected result is 1 item list, current result is: {check_reference}."

        logging.warning("Find Printed Summer Dress.")
        page.find_input_send_keys(locator=automation_practice_back_to_order_history_ids.SEARCH_INPUT_2, input_keys="Printed Summer Dress")

        logging.warning("Click Add to cart.")






