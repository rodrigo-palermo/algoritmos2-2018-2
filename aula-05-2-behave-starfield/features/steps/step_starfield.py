"""Behave Steps File."""

from behave import given, when, then
from starfield import create_star


@given('two positive integer values 0 and 600')
def given1(context):
    """Given two positive integer values 0 and 600')."""
    context.range_int = (0, 600)


@given('a list with values {s1:d}, {s2:d} and {s3:d}')
def given2(context, s1, s2, s3):
    """Given a list with values 1, 2 and 3."""
    context.list = [s1, s2, s3]


@when('I creat an object tha representas a star')
def when1(context):
    """When I creat an object tha representas a star."""
    y_tuple = context.range_int
    speedlist = context.list
    context.result = create_star(y_tuple, speedlist)


@then('the X coord is {x:d}')
def then_x(context, x):
    """Then the X coord is known."""
    waited = x
    observed = context.result[0]
    assert waited == observed


@then('the Y coord is between {y_min:d} and {y_max:d}')
def then_y(context, y_min, y_max):
    """Then the Y coord is betweenknown interval."""
    observed = context.result[1]
    assert (y_min <= observed <= y_max) is True


@then('the star speed is 1, 2 or 3')
def then_speed(context):
    """Then the star speed is 1, 2 or 3."""
    observed = context.result[2]
    assert observed in context.list
