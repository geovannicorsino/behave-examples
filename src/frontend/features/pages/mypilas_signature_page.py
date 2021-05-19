from selenium.webdriver.common.by import By

from src.frontend.features.dictionary import URL
from src.frontend.utils.tools import send_keys, click, select


class MyPilasSignature:
    def __init__(self, context):
        self.context = context
        self.field_email = (By.XPATH, "//input[@type='email']")
        self.field_social = (By.XPATH, "//input[@name='razaoSocial']")
        self.field_cnpj = (By.XPATH, "//input[@name='cnpj']")
        self.field_responsible = (By.XPATH, "//input[@name='responsavel']")
        self.field_password = (By.XPATH, "(//input[@type='password'])[1]")
        self.field_confirm_password = (By.XPATH, "(//input[@type='password'])[2]")
        self.field_calendar = (By.XPATH, "//input[@name='dataFundacao']")
        self.select_state = (By.XPATH, "//select[@name='estado']")
        self.select_city = (By.XPATH, "//select[@id='cidade']")
        self.button_enter = (By.XPATH, "//input[@value='Assinar MyPilas']")

    def open(self, page=None):
        self.context.browser.get(f"{self.context.url_domain}{URL.get(page)}")

    def fill_data(self):
        send_keys(self.context, self.context.user.name, self.field_social)
        send_keys(self.context, "95.178.703/0001-10", self.field_cnpj)
        send_keys(self.context, "23052020", self.field_calendar)
        send_keys(self.context, self.context.user.name, self.field_responsible)
        send_keys(self.context, self.context.user.email, self.field_email)
        select(self.context, self.select_state, "Minas Gerais")
        select(self.context, self.select_city, "Uberlândia")
        send_keys(self.context, self.context.user.password, self.field_password)
        send_keys(self.context, self.context.user.password, self.field_confirm_password)
        click(self.context, self.button_enter)
