import requests

from behave import when


@when(u'i execute the request {endpoint}')
def step_impl(context, endpoint):
    context.response = requests.get(endpoint)
