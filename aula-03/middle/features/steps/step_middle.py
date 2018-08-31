"""Behave Steps for system middle."""

from behave import given, then, when
from middle import middle


@given('a list with the numbers (2, 1, 3)')
def given_a_list1(context):
    """Given a list with 3 numbers."""
    context.a_list = [2, 1, 3]


@when('we want to know the middle one')
def when_get_middle1(context):
    """Get the middle number."""
    list1 = context.a_list
    context.get_middle = middle(list1)


@then('the outcome is 2')
def then_verify_outcome1(context):
    """Verify the outcome."""
    assert(context.get_middle == 2)


@given('a list with the numbers (50, -27, -58)')
def given_a_list2(context):
    """Given a list with 3 numbers."""
    context.a_list = [50, -27, -58]


@then('the outcome is -27')
def then_verify_outcome2(context):
    """Verify the outcome."""
    assert(context.get_middle == -27)


@given('a list with the numbers (125, 219, 198)')
def given_a_list3(context):
    """Given a list with 3 numbers."""
    context.a_list = [125, 219, 198]


@then('the outcome is 198')
def then_verify_outcome3(context):
    """Verify the outcome."""
    assert(context.get_middle == 198)
