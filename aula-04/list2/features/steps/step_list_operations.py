"""Step file for BDD tests."""

from behave import given, when, then
from sistema import *


@given('the list [1,2,3]')
def given_a_list(context):
    """Given the list [1,2,3]."""
    context.a_list = [1, 2, 3]


@when('we want to know the biggest and its index')
def when_biggest(context):
    """When we want to know the biggest and its index."""
    context.biggest = biggest(context.a_list)


@then('the outcome is "Biggest: 3, Index: 2"')
def then_biggest(context):
    """Then the outcome is 'Biggest: 3, Index: 2'."""
    assert(context.biggest == [2, 3])


@when('we want to know the smallest and its index')
def when_smallest(context):
    """When we want to know the smallest and its index."""
    context.smallest = smallest(context.a_list)


@then('the outcome is "Smallest: 1, Index: 0"')
def then_smallest(context):
    """Then the outcome is Smallest: 1, Index: 0'."""
    assert(context.smallest == [0, 1])


@when('we want to know the sum of the even numbers')
def when_sum_of_even(context):
    """When we want to know the sum of the even numbers."""
    context.sum_of_even = sum_of_even(context.a_list)


@then('the outcome is "Sum of even numbers: 2"')
def then_sum_of_even(context):
    """Then the outcome is 'Sum of even numbers: 2'."""
    assert(context.sum_of_even == 2)


@when('we want to know the sum of the odd numbers')
def when_sum_of_odd(context):
    """When we want to know the sum of the odd numbers."""
    context.sum_of_odd = sum_of_odd(context.a_list)


@then('the outcome is "Sum of odd numbers: 4"')
def then_sum_off_odd(context):
    """Then the outcome is 'Sum of odd numbers: 4'."""
    assert(context.sum_of_odd == 4)


@when('we want to know the sum of the even divided by sum of the odd')
def when_division_of_sum(context):
    """When we want to know the sum of the even divided by sum of the odd."""
    context.division_of_sum = division_of_sum(context.a_list)


@then('the outcome is 0.5')
def then_division_of_sum(context):
    """Then the outcome is 0.5."""
    assert(context.division_of_sum == 0.5)


@when('we want to know the list in its inverse order')
def when_inverse(context):
    """When we want to know the list in its inverse order."""
    context.get_inverse = get_inverse(context.a_list)


@then('the outcome is "Inverse order list: [3, 2, 1]"')
def then_inverse(context):
    """Then the outcome is 'Inverse order list: [3, 2, 1]'."""
    assert(context.get_inverse == [3, 2, 1])
