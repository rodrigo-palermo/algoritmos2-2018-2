"""Starfield methods."""

import random


def create_star(**kwargs):
    """Create a star given X (or X range), Y (or Y range) and speed list."""
    if type(kwargs['x']) == int:
        x = kwargs['x']
    else:
        x_range = kwargs['x']
        x = random.randint(x_range[0], x_range[1])

    if type(kwargs['y']) == int:
        y = kwargs['y']
    else:
        y_range = kwargs['y']
        y = random.randint(y_range[0], y_range[1])

    v = random.choice(kwargs['v'])

    # print("coord x = {}. Type: {}".format(x, type(x)))
    # print("coord y = {}. Type: {}".format(y, type(y)))
    # print("vel v = {}. Type: {}".format(v, type(y)))

    return {'x': x, 'y': y, 'v': v}


def move_star(star):
    """Move a star."""
    star['x'] += star['v']


def create_stars_list(quantity, **kwargs):
    """Create a list of stars."""
    index = 0
    stars_list = []
    while index < quantity:
        stars_list.append(create_star(**kwargs))
        index += 1
    return stars_list


def move_stars(stars_list):
    """Move all the stars given a list of stars."""
    for i in range(len(stars_list)):
        move_star(stars_list[i])


# star1 = create_star(x=123, y=[12, 52], v=[1, 2, 3])
# print(star1)
# move_star(star1)
# print(star1)
stars_list1 = create_stars_list(20, x=800, y=[0, 600], v=[1, 2, 3])
print(stars_list1)
