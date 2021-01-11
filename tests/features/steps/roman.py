from behave import *
from src.sample.roman_class import *
from assertpy import assert_that


@given("a decimal number equal to 5")
def step_impl(context):
    context.decimal = 5


@when("the roman numeral is generated")
def step_impl(context):
    context.roman_numeral = roman(context.decimal)


@then("roman numeral should be V")
def step_impl(context):
    assert_that(context.roman_numeral).is_equal_to("V")
