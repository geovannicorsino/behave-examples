from src.frontend.dictionary import MYPiLAS_LOGIN, MYPiLAS_SIGNATURE
from src.frontend.pages.login_page import Login
from src.frontend.pages.signature_page import Signature


class BasePage:
    def __init__(self, context):
        self.context = context
        self.pages = dict({
            (MYPiLAS_LOGIN, Login(context.driver)),
            (MYPiLAS_SIGNATURE, Signature(context.driver))
        })

    def get_page(self, page):
        return self.pages.get(page)
