from behave import *
from main import feature

@given('')
def given_impl(context):
    pass

@when('')
def when_impl(context):
    assert (main("") is True)

@then('')
def then_impl(context):
