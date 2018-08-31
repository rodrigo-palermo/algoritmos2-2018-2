"""Step file for Behave BDD."""

from behave import given, then, when
from collision import is_collided


@given('two rectangles on coordinates (6,7) (7,8) and dimensions (2,2) (2,2)')
def given_rectangles1(context):
    """Given two rectangles on knonw coordinates."""
    context.rectangle1 = {'x': 6, 'y': 7, 'width': 2, 'height': 2}
    context.rectangle2 = {'x': 7, 'y': 8, 'width': 2, 'height': 2}


@when('we want to know if the rectangles collided')
def when_get_positions(context):
    """When we want to know if the rectangles collided."""
    rect1 = context.rectangle1
    rect2 = context.rectangle2
    context.is_collided = is_collided(rect1, rect2)


@then('the outcome is true.')
def then_verify_outcome1(context):
    """Then verify the outcome."""
    assert(context.is_collided is True)


@given('two rectangles on coordinates (6,7) (2,5) and dimensions (2,2) (2,2)')
def given_rectangles2(context):
    """Given two rectangles on knonw coordinates."""
    context.rectangle1 = {'x': 6, 'y': 7, 'width': 2, 'height': 2}
    context.rectangle2 = {'x': 2, 'y': 5, 'width': 2, 'height': 2}


@then('the outcome is false.')
def then_verify_outcome2(context):
    """Then verify the outcome."""
    assert(context.is_collided is False)
