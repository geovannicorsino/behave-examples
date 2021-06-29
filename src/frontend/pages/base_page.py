from src.frontend.dictionary import MYPiLAS_LOGIN, MYPiLAS_SIGNATURE
from src.frontend.pages.mypilas_login_page import MyPilasLogin
from src.frontend.pages.mypilas_signature_page import MyPilasSignature


class BasePage:
    def __init__(self, context):
        self.context = context
        self.pages = dict({
            (MYPiLAS_LOGIN, MyPilasLogin(context)),
            (MYPiLAS_SIGNATURE, MyPilasSignature(context))
        })

    def get_page(self, page):
        return self.pages.get(page)


class Page:
    def __init__(self, context, url=''):
        self.context = context
        self.url = url

    def open(self):
        self.context.browser.get(self.url)
