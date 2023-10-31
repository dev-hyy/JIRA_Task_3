from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Page):
    EMAIL_INPUT_FIELD = (By.ID, 'email-2')
    PASSWORD_INPUT_FIELD = (By.ID, 'field')
    SIGN_IN_BTN = (By.CSS_SELECTOR, 'a.login-button.w-button')

    def open_main(self):
        self.driver.get('https://soft.reelly.io/sign-in')

    def sign_in(self, email, password):
        self.driver.wait = WebDriverWait(self.driver, 3)

        self.driver.wait.until(EC.visibility_of_any_elements_located(self.EMAIL_INPUT_FIELD), message='Email Input Field not clickable')
        self.input_text(email, *self.EMAIL_INPUT_FIELD)

        self.driver.wait.until(EC.visibility_of_any_elements_located(self.PASSWORD_INPUT_FIELD), message='Password Input Field not clickable')
        self.input_text(password, *self.PASSWORD_INPUT_FIELD)

        self.click(*self.SIGN_IN_BTN)
