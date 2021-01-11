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


@given("a decimal number equal to 24")
def step_impl(context):
    context.decimal = 24


@then("roman numeral should be XXIV")
def step_impl(context):
    assert_that(context.roman_numeral).is_equal_to("XXIV")


@given("a decimal number equal to 163")
def step_impl(context):
    context.decimal = 163


@then("roman numeral should be CLXIII")
def step_impl(context):
    assert_that(context.roman_numeral).is_equal_to("CLXIII")


@given("a decimal number equal to 402")
def step_impl(context):
    context.decimal = 402


@then("roman numeral should be CDII")
def step_impl(context):
    assert_that(context.roman_numeral).is_equal_to("CDII")


@given("a decimal number equal to 911")
def step_impl(context):
    context.decimal = 911


@then("roman numeral should be CMXI")
def step_impl(context):
    assert_that(context.roman_numeral).is_equal_to("CMXI")