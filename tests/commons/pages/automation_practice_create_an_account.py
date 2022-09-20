class Xpath:
    DROPDOWN_YEARS = "//select[@id='years']/option[@value='2003']"
    COUNTRY_SELECTOR = "//select[@id='id_country']/option[@value='21']"
    REGISTER_INPUT_XPATH = "//button[@id='submitAccount']/span"
    REegisterBUTTON ="//html//body[@id='authentication']"

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
    MOBILE_PHONE_INPUT_ID = "phone_mobile"
    ADDRRESS_EMAI_INPU = "alias"
    COUNTRY_SELECTOR_ID = "uniform-id_country"
    REGISTER_BUTTON = "submitAccount"


def dropdown_day(value: int):
    return f"//select[@id='days']/option[@value='{value}']"

def dropdown_months(value: int):
    return f"//select[@id='months']/option[@value='{value}']"

def dropdown_years(value: int):
    return f"//select[@id='years']/option[@value='{value}']"

def state_selector(value: str):
    return f"//select[@id='id_state']//*[contains(text(),'{value.capitalize()}')]"

def country_selector(country: str):
    return f"//select[@id='id_country']/option[contains(text(),'{country.title()}')]"


