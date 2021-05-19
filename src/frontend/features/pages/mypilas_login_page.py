from selenium.webdriver.common.by import By

from src.frontend.features.dictionary import URL
from src.frontend.utils.tools import send_keys, click


class MyPilasLogin:
    def __init__(self, context):
        self.context = context
        self.field_email = (By.XPATH, "//input[@type='email']")
        self.field_password = (By.XPATH, "//input[@type='password']")
        self.button_enter = (By.XPATH, "//a[contains(text(), 'Entrar')]")

    def open(self, page=None):
        self.context.browser.get(f"{self.context.url_domain}{URL.get(page)}")

    def fill_data(self):
        send_keys(self.context, self.context.user.email, self.field_email)
        send_keys(self.context, self.context.user.password, self.field_password)
        click(self.context, self.button_enter)
