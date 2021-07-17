import os

from selenium.webdriver.common.by import By

from src.frontend.dictionary import MYPILAS_URL
from src.frontend.pages.page_object import PageObjectModel


class Signature(PageObjectModel):
    URL = f"{MYPILAS_URL}/assine.html"

    def __init__(self, driver):
        super().__init__(driver, url=self.URL)
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

    def fill_data(self, context):
        self.send_keys(context.user.name, self.field_social)
        self.send_keys("95.178.703/0001-10", self.field_cnpj)
        self.send_keys("23052020", self.field_calendar)
        self.send_keys(context.user.name, self.field_responsible)
        self.send_keys(context.user.email, self.field_email)
        self.select(self.select_state, "Minas Gerais")
        self.select(self.select_city, "Uberlândia")
        self.send_keys(context.user.password, self.field_password)
        self.send_keys(context.user.password, self.field_confirm_password)
        self.click(self.button_enter)
