class Xpath:
    pass


class Ids:
    FIRST_NAME = "firstname"
    LAST_NAME = "lastname"
    EMAIL_ID = "email"


def day_xpath(day):
    return f"//select[@id='days']/option[@value='{day}']"


def month_xpath(months):
    return f"//select[@id='months']/option[@value='{months}']"


def year_xpath(years):
    return f"//select[@id='years']/option[@value='{years}']"
