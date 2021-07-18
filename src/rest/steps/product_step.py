import json

from assertpy import assert_that
from behave import then


@then(u'I will have a list of pasta')
def step_impl(context):
    assert_that(200).is_equal_to(context.response.status_code)
    assert_that(bool(json.loads(context.response.text))).is_true()
    for product in json.loads(context.response.text):
        assert_that(float(product['price'])).is_greater_than(0)
        assert_that(float(product['id'])).is_greater_than(0)
        assert_that(product['name']).is_not_empty()
