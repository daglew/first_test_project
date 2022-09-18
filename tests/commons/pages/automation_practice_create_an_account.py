class Xpath:
    DROPDOWN_YEARS = "//select[@id='years']/option[@value='2003']"
    pass

class Ids:
    RADIO_BUTTON_PERSONAL_INF = "id_gender2"
    FIRST_NAME_INPUT_ID = "customer_firstname"
    LAST_NAME_INPUT_ID = "customer_lastname"
    INPUT_EMAIL_ID = "email"
    INPUT_PASSWORD_ID = "passwd"
    SELECTOR_DAY_ID = "uniform-days"

    CHECKBOX_NEWSLETTER = "uniform-newsletter"
    CHECKBOX_RECEIVE_SPECIAL_OFFERTS = "uniform-optin"

    FIRST_NAME_INPUT_ID_2 = "customer_firstname"
    LAST_NAME_INPUT_ID_2 = "lastname"
    ADDRESS_INPUT = "address1"
    CITY_INPUT = "city"
    ZIP_CODE_INPUT = "postcode"
    STATE_SELECTOR = "uniform-id_state"


def dropdown_day(value: int):
    return f"//select[@id='days']/option[@value='{value}']"

def dropdown_months(value: int):
    return f"//select[@id='months']/option[@value='{value}']"

def dropdown_years(value: int):
    return f"//select[@id='years']/option[@value='{value}']"

def state_selector(value: int):
    return f"//select[@id='id_state']/option[@value='{value}']"
