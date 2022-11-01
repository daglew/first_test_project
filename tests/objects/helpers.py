from tests.objects.pages.automation_practice_order_history_page import AutomationPracticeOrderHistoryPage
from tests.objects.pages.automation_practice_order_payment_back_to_orders_page import \
    AutomationPracticeOrderPaymentBackToOrders
from tests.objects.pages.automation_practice_page import AutomationPracticePage
from tests.commons.pages.automation_practice_order_search import Xpath as automation_practice_order_search_xpath
from tests.commons.pages.automation_practice_order_search import Ids as automation_practice_order_search_ids
from tests.objects.pages.automation_practice_order_my_my_store_payment_method_page import \
    AutomationPracticeOrderMyStorePaymentMethod
from tests.objects.pages.automation_practice_order_my_store_address_page import \
    AutomationPracticeOrderMyStoreAddressPage
from tests.objects.pages.automation_practice_order_my_store_page import AutomationPracticeOrderMyStorePage
from tests.commons.pages.automation_practice_order_my_store import Ids as automation_practice_order_my_store_ids
from tests.objects.pages.automation_practice_order_payment_confirm_my_order_page import \
    AutomationPracticeOrderPaymentConfirmMyOrder
from tests.objects.pages.automation_practice_order_search_page import AutomationPracticeOrderSearch
from tests.commons.pages.automation_practice_order_my_store import Xpath as automation_practice_order_my_store_xpath
from tests.commons.pages.automation_practice_order_my_store_address import Xpath as automation_practice_order_my_store_address_xpath
from tests.commons.pages.automation_practice_order_my_my_store_payment_method import \
    Xpath as automation_practice_order_my_my_store_payment_method_xpath, pay_by_check
from tests.commons.pages.automation_practice_order_payment_confirm_my_order import Xpath as automation_practice_order_payment_confirm_my_order_xpath
from tests.commons.pages.automation_practice_order_payment_back_to_orders import Xpath as automation_practice_order_payment_back_to_orders_xpath
from tests.commons.pages.automation_practice_order_history import Xpath as automation_practice_order_history_xpath


def create_user(driver, title, name, last_name, email, password, number_day, number_months, number_years, address,
                city, state, zip_code, information, home_number, selector_country, mobile_phone,
                receive_special_offers=True, sign_up_newsletter=True):
    page = AutomationPracticePage(driver)
    page.open_page()
    page = page.click_sign_in_button()
    page.enter_email(email=email)
    page = page.click_create_an_account_button()
    name = name
    last_name = last_name
    page.fulfill_formula(title=title,
                         first_name=name,
                         last_name=last_name,
                         email=email,
                         password=password,
                         number_day=number_day,
                         number_months=number_months,
                         number_years=number_years,
                         address=address,
                         city=city,
                         state=state,
                         zip_code=zip_code,
                         information=information,
                         home_number=home_number,
                         selector_country=selector_country,
                         mobile_phone=mobile_phone,
                         receive_special_offers=receive_special_offers,
                         sign_up_newsletter=sign_up_newsletter)
    page = page.click_register_button()
    page.assert_user_log_in(name=name, last_name=last_name)
    return page


def create_and_add_to_card(driver, input_keys: str):
    page = AutomationPracticeOrderSearch(driver=driver)
    page.find_input_send_keys(locator=automation_practice_order_search_ids.INPUT_SEARCH,
                              input_keys=input_keys)
    page.find_and_click(locator=automation_practice_order_search_xpath.SEARCH_BUTTON)
    page.click_add_to_cart(input_keys)
    page.confirm_order()
    return page


def create_order(driver, payment_method: str, add_to_card=True, input_keys: str = None):
    if add_to_card:
        create_and_add_to_card(driver=driver, input_keys=input_keys)
    page = AutomationPracticeOrderMyStorePage(driver=driver)
    page.find_and_click(locator=automation_practice_order_my_store_xpath.PROCEED_TO_CHECKOUT_BUTTON)

    page = AutomationPracticeOrderMyStoreAddressPage(driver=driver)
    page.find_and_click(locator=automation_practice_order_my_store_address_xpath.PROCEED_TO_CHECKOUT_ADDRESS_BUTTON)

    page = AutomationPracticeOrderMyStorePage(driver=driver)
    page.find_and_click(locator=automation_practice_order_my_store_ids.TEMS_OF_SERVICE_INPUT)
    page.find_and_click(locator=automation_practice_order_my_store_xpath.PROCEED_TO_CHECKOUT_SHIPPING_BUTTON)

    page = AutomationPracticeOrderMyStorePaymentMethod(driver=driver)
    page.open_page(not_getting_page=True)
    page.pay_method(payment_method)

    page = AutomationPracticeOrderPaymentConfirmMyOrder(driver=driver)
    page.open_page()
    page.find_and_click(locator=automation_practice_order_payment_confirm_my_order_xpath.I_CONFIRM_MY_ORDER_BUTTON)
    return page


def back_orders_and_check_visible_order(driver, number_of_orders: int):
    page = AutomationPracticeOrderPaymentBackToOrders(driver=driver)
    page.open_page(not_getting_page=True)
    page.find_and_click(locator=automation_practice_order_payment_back_to_orders_xpath.BACK_TO_ORDERS)

    page = AutomationPracticeOrderHistoryPage(driver=driver)
    page.open_page()
    check_reference = page.find_elements(locator=automation_practice_order_history_xpath.ORDER_REFERENCE)
    assert len(check_reference) == number_of_orders, f"Expected result is {number_of_orders} " \
                                                       f"item list, current result is: {len(check_reference)}."
    return page
