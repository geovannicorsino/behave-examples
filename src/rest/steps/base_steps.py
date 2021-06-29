from behave import given, when, then

from src.rest.factory.dictionary import endpoints
from src.rest.factory.products import validate_price_products


@given(u'what i have the "{endpoint}"')
def step_impl(context, endpoint):
    context.endpoint = endpoints.get(endpoint)


@when(u'read the prices')
def step_impl(context):
    context.isPriceOk = validate_price_products(context)


@then(u'I will not have any product with zero or lower price')
def step_impl(context):
    assert True == context.isPriceOk
