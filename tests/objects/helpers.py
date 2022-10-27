from tests.objects.pages.automation_practice_page import AutomationPracticePage


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

