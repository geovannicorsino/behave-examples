import os

from selenium.webdriver.common.by import By

from src.frontend.pages.page_object import PageObjectModel


class Login(PageObjectModel):
    URL = f"{os.environ.get('FRONT_URL')}/login.html"

    def __init__(self, driver):
        super().__init__(driver, url=self.URL)
        self.field_email = (By.XPATH, "//input[@type='email']")
        self.field_password = (By.XPATH, "//input[@type='password']")
        self.button_enter = (By.XPATH, "//a[contains(text(), 'Entrar')]")

    def fill_data(self, context):
        self.send_keys(context.user.email, self.field_email)
        self.send_keys(context.user.password, self.field_password)
        self.click(self.button_enter)
