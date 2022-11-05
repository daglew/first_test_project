import logging
import uuid

from tests.commons.data import TestData
from tests.objects.helpers import create_user, create_order, back_orders_and_check_visible_order, create_and_add_to_card
from tests.objects.initialize_webdriver import InitializeWebDriver


class TestOrder(InitializeWebDriver):

    """
    1. Create user.
    2. Click Order history and details tab.
    3. Check if alert warning is visible.
    """
    def test_order_history_no_item_ordered(self):
        logging.warning("Create user.")
        uniqe_id = str(uuid.uuid4())
        generated_email = f"kazia{uniqe_id[:5]}@gmail.com"

        page = create_user(driver=self.driver,
                           title=TestData.TITLE,
                           name=TestData.NAME,
                           last_name=TestData.LAST_NAME,
                           email=generated_email,
                           password=TestData.PASSWORD,
                           number_day=TestData.NUMBER_DAY,
                           number_months=TestData.NUMBER_MONTHS,
                           number_years=TestData.NUMBER_YEARS,
                           address=TestData.ADDRESS,
                           city=TestData.CITY,
                           state=TestData.STATE,
                           zip_code=TestData.ZIP_CODE,
                           information=TestData.INFORMATION,
                           home_number=TestData.HOME_NUMBER,
                           selector_country=TestData.SELECTOR_CUNTRY,
                           mobile_phone=TestData.MOBILE_PHONE,
                           receive_special_offers=True,
                           sign_up_newsletter=True)

        logging.warning("Click Order history and details tab.")
        page = page.click_order_history_and_details()

        logging.warning("Check if alert warning is visible.")
        page.check_alert_warning_visible()

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
        logging.warning("Create user.")
        uniqe_id = str(uuid.uuid4())
        generated_email = f"kazia{uniqe_id[:5]}@gmail.com"

        page = create_user(driver=self.driver,
                           title=TestData.TITLE,
                           name=TestData.NAME,
                           last_name=TestData.LAST_NAME,
                           email=generated_email,
                           password=TestData.PASSWORD,
                           number_day=TestData.NUMBER_DAY,
                           number_months=TestData.NUMBER_MONTHS,
                           number_years=TestData.NUMBER_YEARS,
                           address=TestData.ADDRESS,
                           city=TestData.CITY,
                           state=TestData.STATE,
                           zip_code=TestData.ZIP_CODE,
                           information=TestData.INFORMATION,
                           home_number=TestData.HOME_NUMBER,
                           selector_country=TestData.SELECTOR_CUNTRY,
                           mobile_phone=TestData.MOBILE_PHONE,
                           receive_special_offers=True,
                           sign_up_newsletter=True)

        logging.warning("Click Order history and details tab.")
        page = page.click_order_history_and_details()

        logging.warning("Check if alert warning is visible.")
        page.check_alert_warning_visible()

        logging.warning("Find Faded Short Sleeve T-shirts.")
        logging.warning("Click Add to cart.")
        logging.warning("Confirm order.")
        logging.warning("Confirm summary.")
        logging.warning("Confirm address.")
        logging.warning("Mark agreement and confirm shipping.")
        logging.warning("Choose and click payment method.")
        logging.warning("Confirm order.")
        create_order(driver=self.driver,
                     input_keys=TestData.ORDER_INPUT_KEYS,
                     payment_method=TestData.PAYMENT_METHOD)

        logging.warning("Back to orders")
        logging.warning("Check if new order is visible in order reference column.")
        back_orders_and_check_visible_order(driver=self.driver,
                                            number_of_orders=TestData.VISIBLE_ORDER_1)

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
        logging.warning("Create user.")
        uniqe_id = str(uuid.uuid4())
        generated_email = f"kazia{uniqe_id[:5]}@gmail.com"

        page = create_user(driver=self.driver,
                           title=TestData.TITLE,
                           name=TestData.NAME,
                           last_name=TestData.LAST_NAME,
                           email=generated_email,
                           password=TestData.PASSWORD,
                           number_day=TestData.NUMBER_DAY,
                           number_months=TestData.NUMBER_MONTHS,
                           number_years=TestData.NUMBER_YEARS,
                           address=TestData.ADDRESS,
                           city=TestData.CITY,
                           state=TestData.STATE,
                           zip_code=TestData.ZIP_CODE,
                           information=TestData.INFORMATION,
                           home_number=TestData.HOME_NUMBER,
                           selector_country=TestData.SELECTOR_CUNTRY,
                           mobile_phone=TestData.MOBILE_PHONE,
                           receive_special_offers=True,
                           sign_up_newsletter=True)

        logging.warning("Click Order history and details tab.")
        page = page.click_order_history_and_details()

        logging.warning("Check if alert warning is visible.")
        page.check_alert_warning_visible()

        logging.warning("Find Faded Short Sleeve T-shirts.")
        logging.warning("Click Add to cart.")
        logging.warning("Confirm order.")
        create_and_add_to_card(driver=self.driver,
                               input_keys=TestData.ORDER_INPUT_KEYS)

        logging.warning("Find Faded Blouses.")
        logging.warning("Click Add to cart.")
        logging.warning("Confirm order.")
        create_and_add_to_card(driver=self.driver,
                               input_keys=TestData.ORDER_INPUT_KEYS_2)

        logging.warning("Confirm summary.")
        logging.warning("Confirm address.")
        logging.warning("Mark agreement and confirm shipping.")
        logging.warning("Choose and click payment method.")
        logging.warning("Confirm order.")
        create_order(driver=self.driver,
                     payment_method=TestData.PAYMENT_METHOD,
                     add_to_card=False)
        logging.warning("Back to orders")
        logging.warning("Check if new order is visible in order reference column.")
        back_orders_and_check_visible_order(driver=self.driver,
                                            number_of_orders=TestData.VISIBLE_ORDER_1)

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
        logging.warning("Create user.")
        uniqe_id = str(uuid.uuid4())
        generated_email = f"kazia{uniqe_id[:5]}@gmail.com"

        page = create_user(driver=self.driver,
                           title=TestData.TITLE,
                           name=TestData.NAME,
                           last_name=TestData.LAST_NAME,
                           email=generated_email,
                           password=TestData.PASSWORD,
                           number_day=TestData.NUMBER_DAY,
                           number_months=TestData.NUMBER_MONTHS,
                           number_years=TestData.NUMBER_YEARS,
                           address=TestData.ADDRESS,
                           city=TestData.CITY,
                           state=TestData.STATE,
                           zip_code=TestData.ZIP_CODE,
                           information=TestData.INFORMATION,
                           home_number=TestData.HOME_NUMBER,
                           selector_country=TestData.SELECTOR_CUNTRY,
                           mobile_phone=TestData.MOBILE_PHONE,
                           receive_special_offers=True,
                           sign_up_newsletter=True)

        logging.warning("Click Order history and details tab.")
        page = page.click_order_history_and_details()

        logging.warning("Check if alert warning is visible.")
        page.check_alert_warning_visible()

        logging.warning("Find Faded Short Sleeve T-shirts.")
        logging.warning("Click Add to cart.")
        logging.warning("Confirm order.")
        logging.warning("Confirm summary.")
        logging.warning("Confirm address.")
        logging.warning("Mark agreement and confirm shipping.")
        logging.warning("Choose and click payment method.")
        logging.warning("Confirm order.")
        create_order(driver=self.driver,
                     input_keys=TestData.ORDER_INPUT_KEYS,
                     payment_method=TestData.PAYMENT_METHOD)
        logging.warning("Back to orders")
        logging.warning("Check if new order is visible in order reference column.")
        back_orders_and_check_visible_order(driver=self.driver,
                                            number_of_orders=TestData.VISIBLE_ORDER_1)
        logging.warning("Find Printed Summer Dress.")
        page.find_printed_summer_dress()

        logging.warning("Click Add to cart.")
        logging.warning("Confirm order.")
        logging.warning("Confirm summary.")
        logging.warning("Confirm address.")
        logging.warning("Mark agreement and confirm shipping.")
        logging.warning("Choose and click payment method.")
        logging.warning("Confirm order.")
        create_order(driver=self.driver,
                     input_keys=TestData.ORDER_INPUT_KEYS,
                     payment_method=TestData.PAYMENT_METHOD)

        logging.warning("Back to orders.")
        logging.warning("Verify that both orders appear in the order column.")
        back_orders_and_check_visible_order(driver=self.driver,
                                            number_of_orders=TestData.VISIBLE_ORDER_2)
