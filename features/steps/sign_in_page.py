from telnetlib import EC

from behave import given, when, then
from selenium.webdriver.common.by import By
import time

SEARCH_BTN = (By.ID, 'nav-search-submit-button')
ON_OFF_LINK = (By.CSS_SELECTOR, 'a._1-link-menu.w-inline-block.w--current')
FIRST_PRODUCT_LINK = (By.CSS_SELECTOR, 'a.project-card.w-inline-block')
VISUALIZATION_TAB = (By.CSS_SELECTOR, 'div.tabs-menu-project.w-tab-menu > a')
VISUALIZATION_TAB_SELECTED = (By.CSS_SELECTOR, '[aria-selected="true"]')
ORDERS_BTN = (By.ID, 'nav-orders')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem')
SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')


@given('Open Reely page')
def open_reely(context):
    context.app.main_page.open_main()


@given('User enters login credentials')
def user_login(context):
    context.app.main_page.sign_in('somesurd@gmail.com', '9a$vF4V.)Qv,)>v')


@when('Click Amazon Orders link')
def click_amazon_orders(context):
    context.driver.find_element(*ORDERS_BTN).click()


@when('Click on off plan at the left side menu')
def click_onoff_plan_link(context):
    context.driver.find_element(*ON_OFF_LINK).click()
    time.sleep(1)


@when('Click on the first product')
def click_on_first_product(context):
    context.driver.get('https://soft.reelly.io/project/general?projectid=515')
    time.sleep(3)


@then('Verify there are {expected_result} options for visualization')
def verify_three_options_in_visualization(context, expected_result):

    expected_result = int(expected_result)
    actual_result = len(context.driver.find_elements(*VISUALIZATION_TAB))
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    # context.app.search_result_page.verify_result(expected_result, actual_result)


@then('Verify the three options of visualization are {visualization_type_1}, {visualization_type_2}, {visualization_type_3}')
def verify_can_click_colors(context, visualization_type_1, visualization_type_2, visualization_type_3):
    expected_texts = [visualization_type_1, visualization_type_2, visualization_type_3]
    actual_texts = []

    visualization_types = context.driver.find_elements(*VISUALIZATION_TAB)

    for visualization_type in visualization_types:
        visualization_type.click()
        current_visualization_type = context.driver.find_element(*VISUALIZATION_TAB_SELECTED).text

        actual_texts.append(current_visualization_type)

    assert actual_texts == expected_texts, f'Expected {expected_texts} did not match actual {actual_texts}'


@then('Verify the options of visualization are clickable')
def verify_clickable_visualizations(context):
    visualization_types = context.driver.find_elements(*VISUALIZATION_TAB)

    expected_click_count = 3
    actual_click_count = 0

    for visualization_type in visualization_types:
        visualization_type.click()
        actual_click_count += 1

    assert actual_click_count == expected_click_count, f'Expected {expected_click_count} did not match actual {actual_click_count}'

@then('Verify Sign In page is opened')
def verify_many_links(context):
    context.app.sign_in_page.verify_sign_in_page()
