from behave import *
from src.sample.roman_class import *
from assertpy import assert_that


@given("first strand is empty")
def step_impl(context):
    context.first = ""


@step("second strand is empty")
def step_impl(context):
    context.second = ""


@when("the distance is calculated")
def step_impl(context):
    context.result = context.hamming.distance(context.first, context.second)


@then("the distance should be 0")
def step_impl(context):
    assert_that(context.result).is_equal_to(0)


@given("first strand is A")
def step_impl(context):
    context.first = "A"


@step("second strand is A")
def step_impl(context):
    context.second = "A"