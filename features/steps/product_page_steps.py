from time import sleep

from selenium.webdriver.common.by import By
from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

INDIVIDUAL_VISUALIZATION_TAB = (By.CSS_SELECTOR, 'div.w-tabs > div > a')
VISUALIZATION_TAB1 = (By.ID, 'w-tabs-0-data-w-tab-0')
VISUALIZATION_TAB2 = (By.ID, 'w-tabs-0-data-w-tab-1')
VISUALIZATION_TAB3 = (By.ID, 'w-tabs-0-data-w-tab-2')

VISUALIZATION_TAB1_TEXT = (By.ID, 'w-tabs-0-data-w-tab-0 div:nth-child(1) div:nth-child(1)')
VISUALIZATION_TAB2_TEXT = (By.ID, 'w-tabs-0-data-w-tab-1 div:nth-child(1) div:nth-child(1)')
VISUALIZATION_TAB3_TEXT = (By.ID, 'w-tabs-0-data-w-tab-2 div:nth-child(1) div:nth-child(1)')

# VISUALIZATION_TAB = (By.CSS_SELECTOR, 'div.tabs-menu-project.w-tab-menu > a')
VISUALIZATION_TAB = (By.XPATH, "//div[contains(@class, 'tabs-menu-project w-tab-menu') and contains(@role, 'tablist')] //a")
VISUALIZATION_TAB_SELECTED = (By.CSS_SELECTOR, '[aria-selected="true"]')


@then('Verify there are {expected_result} options for visualization')
def verify_three_options_in_visualization(context, expected_result):
    expected_result = int(expected_result)
    actual_result = len(context.driver.find_elements(*VISUALIZATION_TAB))
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'


@then('Verify the three options of visualization are {visualization_type_1}, {visualization_type_2}, {visualization_type_3}')
def verify_can_click_visualization(context, visualization_type_1, visualization_type_2, visualization_type_3):
    expected_texts = [visualization_type_1, visualization_type_2, visualization_type_3]
    tab1_text = context.driver.find_element(*VISUALIZATION_TAB1_TEXT).text
    tab2_text = context.driver.find_element(*VISUALIZATION_TAB2_TEXT).text
    tab3_text = context.driver.find_element(*VISUALIZATION_TAB3_TEXT).text
    actual_texts = [tab1_text, tab2_text, tab3_text]

    assert actual_texts == expected_texts, f'Expected {expected_texts} did not match actual {actual_texts}'


@then('Verify the options of visualization are clickable')
def verify_clickable_visualizations(context):
    visualization_types = context.driver.find_elements(*INDIVIDUAL_VISUALIZATION_TAB)

    expected_click_count = 3
    actual_click_count = 0

    for visualization_type in visualization_types:
        visualization_type.click()
        actual_click_count += 1

    assert actual_click_count == expected_click_count, f'Expected {expected_click_count} did not match actual {actual_click_count}'

    #####
    # visualization_types = context.driver.find_elements(*VISUALIZATION_TAB)
    #
    # expected_click_count = 3
    # actual_click_count = 0
    #
    # for visualization_type in visualization_types:
    #     visualization_type.click()
    #     actual_click_count += 1
    #
    # assert actual_click_count == expected_click_count, f'Expected {expected_click_count} did not match actual {actual_click_count}'