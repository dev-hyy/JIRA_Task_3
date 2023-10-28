from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    EMAIL_INPUT_FIELD = (By.ID, 'email-2')
    PASSWORD_INPUT_FIELD = (By.ID, 'field')
    SIGN_IN_BTN = (By.CSS_SELECTOR, 'a.login-button.w-button')

    def open_main(self):
        self.driver.get('https://soft.reelly.io/sign-in')

    def sign_in(self, email, password):
        self.input_text(email, *self.EMAIL_INPUT_FIELD)
        self.input_text(password, *self.PASSWORD_INPUT_FIELD)
        self.click(*self.SIGN_IN_BTN)