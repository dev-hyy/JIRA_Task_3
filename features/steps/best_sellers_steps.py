from behave import given, when, then
from selenium.webdriver.common.by import By

BEST_SELLERS_BUTTON = (By.CSS_SELECTOR, "[data-csa-c-content-id='nav_cs_bestsellers']")
LINKS = (By.CSS_SELECTOR, "*[class^='_p13n-zg-nav-tab-all_style_zg-tabs-li']")
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
PRODUCT_LINK = (By.CSS_SELECTOR, '.a-section.a-spacing-base')
ADD_TO_CART = (By.ID, 'add-to-cart-button')
PRODUCT_QUANTITY = (By.ID, 'nav-cart-count')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Best Sellers link')
def search_on_amazon(context):
    context.driver.find_element(*BEST_SELLERS_BUTTON).click()


@then('Verify that there are {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'


@when('Add {product} to cart')
def add_product_to_cart(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_BTN).click()
    context.driver.find_element(*PRODUCT_LINK).click()
    context.driver.find_element(*ADD_TO_CART).click()


@then('Verify that {product} is in cart')
def verify_search_result(context, product):
    expected_result = "1"
    product = context.driver.find_element(*PRODUCT_QUANTITY).text
    assert product == expected_result, f'Error, expected {expected_result} did not match actual {product}'



