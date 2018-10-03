"""Behave Steps File."""

from behave import given, when, then
from starfield import create_star


@given('two positive integer values 0 and 600')
def given1(context):
    """Given two positive integer values 0 and 600')."""
    context.range_int = (0, 600)


@given('a list with values 1, 2 and 3')
def given2(context):
    """Given a list with values 1, 2 and 3."""
    context.list = [1, 2, 3]


@when('I creat an object tha representas a star')
def when1(context):
    """When I creat an object tha representas a star."""
    y_tuple = context.range_int
    speedlist = context.list
    context.result = create_star(y_tuple, speedlist)


@then('the X coord is 800')
def then_x(context):
    """Then the X coord is 800."""
    waited = 800
    observed = context.result[0]
    assert waited == observed


@then('the Y coord is between 0 and 600')
def then_y(context):
    """Then the Y coord is between 0 and 600."""
    observed = context.result[1]
    assert (0 <= observed <= 600) is True


@then('the star speed is 1, 2 or 3')
def then_speed(context):
    """Then the star speed is 1, 2 or 3."""
    observed = context.result[2]
    assert observed in context.list
