from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_TEXT = (By.CSS_SELECTOR, 'div > h1')

    def verify_sign_in_page(self):
        actual_text = self.find_element(*self.SIGN_IN_TEXT).text
        assert actual_text == "Sign in", f'Error, expected Sign In page is not displayed.'
