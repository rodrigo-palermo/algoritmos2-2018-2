"""Verify whether a point is inside of a rectangle."""

from behave import given, when, then
from inside import is_point_in_rectangle


@given('a point with coordinates (7, 8)')
def a_point(context):
    context.point = {'x': 7, 'y': 8}


@given('a rectangle wih coordinates (6, 7) and dimension (2, 2)')
def a_rectangle(context):
    context.rectangle = {'x': 6, 'y': 7, 'width': 2, 'height': 2}


@when('we want to know wheter the point is inside the rectangle')
def step_impl(context):
    pass


@then('the outcome is true.')
def is_inside(context):
    assert(is_point_in_rectangle(context.point, context.rectangle) is True)


@given(u'a point with coordinates (5, 9)')
def a_point2(context):
    context.point = {'x': 5, 'y': 9}


@given(u'a rectangle with coordinates (6, 7) and dimension (2, 3)')
def a_rectangle2(context):
    context.rectangle = {'x': 6, 'y': 7, 'width': 2, 'height': 3}


@when(u'we want to know whether the point is inside the rectangle')
def step_impl2(context):
    pass


@then(u'the outcome is false.')
def is_inside2(context):
    assert(is_point_in_rectangle(context.point, context.rectangle) is False)
