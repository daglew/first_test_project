class Xpath:
    pass

class Ids:
    FIRST_NAME = "firstname"
    LAST_NAME = "lastname"
    EMAIL_ID = "email"



def day_xpath(day):
    return f"//select[@id='days']/option[@value='{day}']"
