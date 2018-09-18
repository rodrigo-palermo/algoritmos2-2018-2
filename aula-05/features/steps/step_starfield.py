"""Step file for BDD test - Display a starfield."""

from behave import given, when, then
from starfield import create_star, move_star, create_stars_list, move_stars

# Senario 1


@given('two positive integer values, 0 and 600')
def given_y_min_range(context):
    """Given two positive integer values, 0 and 600."""
    context.y_min = 0
    context.y_max = 600


@given('a list with values 1, 2 and 3')
def given_speed(context):
    """Given a list with values 1, 2 and 3."""
    context.speed = [1, 2, 3]


@when('I create an object that represents a star')
def when_create_star(context):
    """When I create an object that represents a star."""
    context.star1 = create_star(x=800, y=[context.y_min, context.y_max],
                                s=context.speed)


@then('its X coordinate is 800')
def then_x1(context):
    """Then its X coordinate is 800."""
    assert(context.star1['x'] == 800)


@then('its Y coordinate is between 0 and 600')
def then_y1(context):
    """Then its Y coordinate is between 0 and 600."""
    assert(context.star1['y'] >= 0 and context.star1['y'] <= 600)


@then('its speed is 1, 2 or 3')
def then_v1(context):
    """Then its speed is 1, 2 or 3."""
    assert(context.star1['s'] in [1, 2, 3])


# Scenario 2


@given('an object reresenting a star')
def given_a_star(context):
    """Given an object reresenting a star."""
    context.star1 = create_star(x=800, y=[0, 600],
                                s=[1, 2, 3])
    context.x = context.star1['x']
    context.y = context.star1['y']
    context.s = context.star1['s']


@when('I move the star')
def when_moving(context):
    """When I move the star."""
    move_star(context.star1)


@then('its X coordinate changes according to its speed')
def then_x2(context):
    """Then its X coordinate changes according to its speed."""
    assert(context.star1['x'] == context.x - context.s)


@then('its Y coordinate does not change')
def then_y2(context):
    """Then its Y coordinate does not change."""
    assert(context.star1['y'] == context.y)


@then('its speed does not change')
def then_v2(context):
    """Then its speed does not change."""
    assert(context.star1['s'] == context.s)


# Scenario 3


@when('I create a list with 20 stars')
def when_create_stars(context):
    """When I create a list with 20 stars."""
    context.stars_list = create_stars_list(20, x=800, y=[0, 600], s=[1, 2, 3])


@then('the X coordinate of each star is 800')
def then_x3(context):
    """Then the X coordinate of each star is 800."""
    for i in range(len(context.stars_list['list'])):
        assert(context.stars_list['list'][i]['x'] == 800)


@then('the Y coordinate of each star is between 0 and 600')
def then_y3(context):
    """Then the Y coordinate of each star is between 0 and 600."""
    for i in range(len(context.stars_list['list'])):
        assert(context.stars_list['list'][i]['y'] >= 0 and
               context.stars_list['list'][i]['y'] <= 600)


@then('the speed of each star is 1, 2 or 3')
def then_v3(context):
    """Then the speed of each star is 1, 2 or 3."""
    for i in range(len(context.stars_list['list'])):
        assert(context.stars_list['list'][i]['s'] in [1, 2, 3])


# Scenario 4


@given('a list of objects representing stars')
def given_stars_list(context):
    """Given a list of objects representing stars."""
    context.stars_list = create_stars_list(20, x=800, y=[0, 600], s=[1, 2, 3])


@when('I move the stars in the list')
def when_move_stars_list(context):
    """When I move the stars in the list."""
    move_stars(context.stars_list)


@then('the X coordinate of each star changes according to its speed')
def then_x4(context):
    """Then the X coordinate of each star changes according to its speed."""
    for i in range(len(context.stars_list['list'])):
        assert(context.stars_list['list'][i]['x'] == 800 -
               context.stars_list['list'][i]['s'])


@then('the Y coordinate of each star does not change')
def then_y4(context):
    """Then the Y coordinate of each star does not change."""
    for i in range(len(context.stars_list['list'])):
        assert(context.stars_list['list'][i]['y'] >= 0
               and context.stars_list['list'][i]['y'] <= 600)


@then('the speed of each star does not change')
def then_v4(context):
    """Then the speed of each star does not change."""
    for i in range(len(context.stars_list['list'])):
        assert(context.stars_list['list'][i]['s'] in [1, 2, 3])


# Scenario 5 - INCOMPLETE

@given('a specific list of stars')
def given_stars_list2(context):
    """Given a specific list of stars."""
    # for row in context.table:
    #    context.model.add_user(x=row['x'], y=row['y'], speed=row['speed'])


@when('I move the stars 4 times')
def when_move_4times(context):
    """When I move the stars 4 times."""


@then('the list will have only 2 stars')
def then_last_is_deleted(context):
    """Then the list will have only 2 stars."""
