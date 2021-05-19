from src.frontend.features.dictionary import MYPiLAS_LOGIN
from src.frontend.features.pages.mypilas_login_page import MyPilasLogin


class BasePage:
    def __init__(self, context):
        self.pages = dict({
            (MYPiLAS_LOGIN, MyPilasLogin(context))
        })

    def get_page(self, page):
        return self.pages.get(page)
