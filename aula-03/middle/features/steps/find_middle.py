from behave import given, when, then
from middle import *


@given('a list with the numbers (2, 1, 3)')
def a_list1(context):
    context.a_list = [2, 1, 3]


@when('we want to know the middle one')
def step_impl(context):
    pass


@then('the outcome is 2')
def middle1(context):
    assert(middle(context.a_list) == 2)


@given('a list with the numbers (50, -27, -58)')
def a_list2(context):
    context.a_list = [50, -27, -58]


@then('the outcome is -27')
def middle2(context):
    assert(middle(context.a_list) == -27)


@given('a list with the numbers (125, 219, 198)')
def a_list3(context):
    context.a_list = [125, 219, 198]


@then('the outcome is 198')
def middle3(context):
    assert(middle(context.a_list) == 198)
