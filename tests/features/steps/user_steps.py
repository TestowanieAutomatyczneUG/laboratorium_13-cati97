from behave import *
from src.sample.roman_class import *
from src.sample.user_class import *
from assertpy import assert_that
from src.sample.user_class import *
use_step_matcher("parse")


@given(u'the user wants to create prop first name as "{first_name}"')
def step_impl(context, first_name):
    context.user.firstname = first_name


@step(u'the user wants to create prop last name as "{last_name}"')
def step_impl(context, last_name):
    context.user.lastname = last_name


@when("get_firstname is run")
def step_impl(context):
    context.result = context.user.get_firstname()


@when("get_lastname is run")
def step_impl(context):
    context.result = context.user.get_lastname()


@when("create_fullname is run")
def step_impl(context):
    context.result = context.user.create_fullname(context.user.firstname, context.user.lastname)


@then(u'you should receive "{result}"')
def step_impl(context, result):
    assert_that(context.result).is_equal_to(result)
