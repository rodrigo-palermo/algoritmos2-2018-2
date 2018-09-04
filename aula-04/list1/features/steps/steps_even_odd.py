"""Step file for BDD tests."""

from behave import given, when, then
from sistema import is_even


@given('a knonw list')
def given_a_list(context):
    """Given a knonw list."""
    context.list1 = [0, 1, 2, 3]


@when('we want to know the parity of the numbers in the list')
def when_get_parity(context):
    """Get the parity of the numbers in a list."""
    context.parity_list = is_even(context.list1)


@then('the outcome is [True, False, True, False]')
def then_verify_outcome(context):
    """Return a list with the parity of the numbers in a list."""
    assert context.parity_list == [True, False, True, False]
