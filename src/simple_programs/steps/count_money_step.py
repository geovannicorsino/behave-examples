from assertpy import assert_that
from behave import given, when, then

from src.simple_programs.steps.note import withdraw


@given('what i have {value}')
def step_impl(context, value):
    context.inputMoney = value


@when(u'i count the minimun number of notes')
def step_impl(context):
    context.quantityNotes = withdraw(int(context.inputMoney))


@then(u'i will have {quantity} notes')
def step_impl(context, quantity):
    assert_that(context.quantityNotes).is_equal_to(int(quantity))
