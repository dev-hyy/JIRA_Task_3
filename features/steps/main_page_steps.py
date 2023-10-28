from behave import when
from selenium.webdriver.common.by import By

ON_OFF_LINK = (By.CSS_SELECTOR, 'a._1-link-menu.w-inline-block.w--current')
FIRST_PRODUCT_LINK = (By.CSS_SELECTOR, 'div.cards-properties > a')


@when('Click on off plan at the left side menu')
def click_onoff_plan_link(context):
    context.driver.find_element(*ON_OFF_LINK).click()


@when('Click on the first product')
def click_on_first_product(context):
    context.driver.find_element(*FIRST_PRODUCT_LINK).click()


