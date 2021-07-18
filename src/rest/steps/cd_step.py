import json

import xmltodict
from assertpy import assert_that
from behave import then


@then(u'I will have a list of CDs')
def step_impl(context):
    assert_that(200).is_equal_to(context.response.status_code)
    context.response_body = json.loads(json.dumps(xmltodict.parse(context.response.text)))['CATALOG']['CD']
    for product in context.response_body:
        assert_that(float(product['PRICE'])).is_greater_than(0)
        assert_that(product['TITLE']).is_not_empty()
