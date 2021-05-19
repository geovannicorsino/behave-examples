from src.frontend.features.dictionary import MYPiLAS_LOGIN, MYPiLAS_SIGNATURE
from src.frontend.features.pages.mypilas_login_page import MyPilasLogin
from src.frontend.features.pages.mypilas_signature_page import MyPilasSignature


class BasePage:
    def __init__(self, context):
        self.pages = dict({
            (MYPiLAS_LOGIN, MyPilasLogin(context)),
            (MYPiLAS_SIGNATURE, MyPilasSignature(context))
        })

    def get_page(self, page):
        return self.pages.get(page)
