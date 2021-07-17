from behave import given, when, then

from src.frontend.pages.pages import BasePage


@given(u'what i´m the "{page}"')
def step_impl(context, page):
    context.page = BasePage(context).get_page(page=page)
    context.driver.get(url="https://mypilas-geovanni-geovannicorsino.vercel.app/login.html")
    # context.page.open()


@when(u'to fill in the data')
def step_impl(context):
    context.page.fill_data(context)


@then(u'i did my signature on MyPilas')
def step_impl(context):
    ...


@then(u'i´m online on MyPilas')
def step_impl(context):
    ...
