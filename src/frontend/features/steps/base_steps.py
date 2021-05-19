from behave import given, when, then

from src.frontend.features.pages.base_page import BasePage


@given(u'what i´m the "{page}"')
def step_impl(context, page):
    context.page = BasePage(context).get_page(page=page)
    context.page.open(page)


@when(u'to fill in the data')
def step_impl(context):
    context.page.fill_data()


@then(u'i did my signature on MyPilas')
def step_impl(context):
    ...


@then(u'i´m online on MyPilas')
def step_impl(context):
    ...
