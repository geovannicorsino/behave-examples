from src.frontend.features.dictionary import MYPILAS_URL
from src.frontend.setup import setup_browser


def before_all(context):
    context.scenarios = []


def before_scenario(context, scenario):
    context.browser = setup_browser(context)
    context.url_domain = MYPILAS_URL


def after_scenario(context, scenario):
    context.scenarios.append(scenario)
