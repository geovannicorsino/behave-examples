from dotenv import load_dotenv

from src.frontend.dictionary import MYPILAS_URL
from src.frontend.factory.fake_data import User
from src.frontend.utils.setup import setup_browser


def before_all(context):
    load_dotenv()
    context.scenarios = []


def before_scenario(context, scenario):
    context.url_domain = MYPILAS_URL
    context.user = User()
    context.browser = setup_browser(context)


def after_scenario(context, scenario):
    context.browser.quit()
    context.scenarios.append(scenario)
