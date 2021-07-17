import json
import requests

import xmltodict
from assertpy import assert_that
from behave import when, then


@when(u'i execute the request {endpoint}')
def step_impl(context, endpoint):
    context.response = requests.get(endpoint)


@then(u'I will have a list of CDs')
def step_impl(context):
    assert_that(200).is_equal_to(context.response.status_code)
    context.response_body = json.loads(json.dumps(xmltodict.parse(context.response.text)))['CATALOG']['CD']
    for product in context.response_body:
        context.cd = product


@then(u'no CD with zero or lower price')
def step_impl(context):
    assert_that(float(context.cd['PRICE'])).is_greater_than(0)


@then(u'no CD with empty title')
def step_impl(context):
    assert_that(context.cd['TITLE']).is_not_empty()
