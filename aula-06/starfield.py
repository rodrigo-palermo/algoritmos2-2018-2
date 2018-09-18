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
    if type(kwargs['s']) == int:
        s = kwargs['s']
    else:
        s = random.choice(kwargs['s'])

    return {'x': x, 'y': y, 's': s}


def move_star(star):
    """Move a star."""
    star['x'] -= star['s']


def create_stars_list(quantity, **kwargs):
    """Create a list of stars."""
    index = 0
    moves = 0
    stars_list = []
    while index < quantity:
        stars_list.append(create_star(**kwargs))
        index += 1
    return {'list': stars_list, 'moves': moves}


def move_stars(stars_list):
    """Move all the stars given a dictionary of stars {'moves', 'list'}."""
    stars_list['moves'] += 1
    if stars_list['moves'] == 4:
        stars_list['moves'] = 0
        if len(stars_list['list']) > 0:
            stars_list['list'].pop(0)
    if len(stars_list['list']) > 0:
        for i in range(len(stars_list['list'])):
            move_star(stars_list['list'][i])
