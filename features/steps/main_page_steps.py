from telnetlib import EC

from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
ORDERS_BTN = (By.ID, 'nav-orders')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem')
SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('Click Amazon Orders link')
def click_amazon_orders(context):
    context.driver.find_element(*ORDERS_BTN).click()


@then('Verify Sign In page is opened')
def verify_many_links(context):
    context.app.sign_in_page.verify_sign_in_page()

