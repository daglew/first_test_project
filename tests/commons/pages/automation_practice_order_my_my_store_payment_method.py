class Xpath:
    PAY_BY_BANK_INPUT = "//a[@title='Pay by bank wire']"
    PAY_BY_CHECK_INPUT = "//a[@title='Pay by check.']"


class Ids:
    pass


def pay_by_check(check_pay):
    return f"//a[@title='{check_pay}']"
