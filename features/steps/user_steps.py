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


@step(u'the user wants to create prop user_id as "{user_id}"')
def step_impl(context, user_id):
    context.user.user_id = user_id


@step(u'the user wants to create prop email as "{email}"')
def step_impl(context, email):
    context.user.email = email


@step(u'the user wants to create prop phone as "{phone}"')
def step_impl(context, phone):
    context.user.phone = int(phone)


@when("get_firstname is run")
def step_impl(context):
    context.result = context.user.get_firstname()

@when("check_phone_is_int is run")
def step_impl(context):
    context.result = context.user.check_phone_is_int()

@when("check_user_id_is_length_four is run")
def step_impl(context):
    context.result = context.user.check_user_id_is_length_four()


@when("get_lastname is run")
def step_impl(context):
    context.result = context.user.get_lastname()


@when("check_email_is_correct is run")
def step_impl(context):
    context.result = context.user.check_email_is_correct()


@when("create_fullname is run")
def step_impl(context):
    context.result = context.user.create_fullname(context.user.firstname, context.user.lastname)


@then(u'you should receive "{result}"')
def step_impl(context, result):
    assert_that(str(context.result)).is_equal_to(result)
