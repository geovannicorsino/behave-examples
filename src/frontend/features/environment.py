from src.frontend.features.dictionary import MYPILAS_URL
from src.frontend.features.factory.fake_data import User
from src.frontend.utils.setup import setup_browser


def before_all(context):
    context.scenarios = []


def before_scenario(context, scenario):
    context.browser = setup_browser(context)
    context.url_domain = MYPILAS_URL
    context.user = User()


def after_scenario(context, scenario):
    context.browser.quit()
    context.scenarios.append(scenario)
