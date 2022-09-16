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

def dropdown_day(value: int):
    return f"//select[@id='days']/option[@value='{value}']"

def dropdown_months(value: int):
    return f"//select[@id='months']/option[@value='{value}']"

def dropdown_years(value: int):
    return f"//select[@id='years']/option[@value='{value}']"
