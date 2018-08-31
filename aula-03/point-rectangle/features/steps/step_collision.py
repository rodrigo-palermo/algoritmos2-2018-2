"""Step file for Behave BDD."""

from behave import given, then, when
from collision import is_point_in_rectangle


@given('a point with coordinates (7, 8)')
def given_point1(context):
    """Given a point with known coordinates."""
    context.point = {'x': 7, 'y': 8}


@given('a rectangle wih coordinates (6, 7) and dimension (2, 2)')
def given_rectangle1(context):
    """Given a rectangle wih known coordinates."""
    context.rectangle = {'x': 6, 'y': 7, 'width': 2, 'height': 2}


@when('we want to know whether the point is inside the rectangle')
def when_calculate_collision(context):
    """When we want to know whether the point is inside the rectangle."""
    point = context.point
    rectangle = context.rectangle
    context.collided = is_point_in_rectangle(point, rectangle)


@then('the outcome is true.')
def then_verify_outcome1(context):
    """Then verify the outcome."""
    assert(context.collided is True)


@given('a point with coordinates (5, 9)')
def given_point2(context):
    """Given a point with known coordinates."""
    context.point = {'x': 5, 'y': 9}


@given('a rectangle with coordinates (6, 7) and dimension (2, 3)')
def given_rectangle2(context):
    """Given a rectangle wih known coordinates."""
    context.rectangle = {'x': 6, 'y': 7, 'width': 2, 'height': 2}


@then('the outcome is false.')
def then_verify_outcome2(context):
    """Then verify the outcome."""
    assert(context.collided is False)
