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
    try:
        context.result = context.hamming.distance(context.first, context.second)
    except ValueError as e:
        context.exc = e


@then("the distance should be 0")
def step_impl(context):
    assert_that(context.result).is_equal_to(0)


@given("first strand is A")
def step_impl(context):
    context.first = "A"


@step("second strand is A")
def step_impl(context):
    context.second = "A"


@given("first strand is G")
def step_impl(context):
    context.first = "G"


@step("second strand is T")
def step_impl(context):
    context.second = "T"

@then("the distance should be 1")
def step_impl(context):
    assert_that(context.result).is_equal_to(1)


@given("first strand is AGT")
def step_impl(context):
    context.first = "AGT"


@step("second strand is TGC")
def step_impl(context):
    context.second = "TGC"


@then("the distance should be 2")
def step_impl(context):
    assert_that(context.result).is_equal_to(2)


@given("first strand is AATG")
def step_impl(context):
    context.first = "AATG"


@step("second strand is AAA")
def step_impl(context):
    context.second = "AAA"


@then("ValueError should be raised")
def step_impl(context):
    assert_that(context.exc).is_instance_of(ValueError)


@given("first strand is AC")
def step_impl(context):
    context.first = "AC"


@step("second strand is GTCC")
def step_impl(context):
    context.second = "GTCC"
