from behave import given, when, then

from src.frontend.dictionary import URL
from src.frontend.pages.base_page import BasePage, Page


@given(u'what i´m the "{page}"')
def step_impl(context, page):
    context.page = BasePage(context).get_page(page=page)
    Page(context, URL.get(page)).open()


@when(u'to fill in the data')
def step_impl(context):
    context.page.fill_data()


@then(u'i did my signature on MyPilas')
def step_impl(context):
    ...


@then(u'i´m online on MyPilas')
def step_impl(context):
    ...
