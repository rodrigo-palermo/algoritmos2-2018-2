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

    # print("coord x = {}. Type: {}".format(x, type(x)))
    # print("coord y = {}. Type: {}".format(y, type(y)))
    # print("speed s = {}. Type: {}".format(s, type(y)))

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
    """Move all the stars given a list of stars."""
    stars_list['moves'] += 1
    if stars_list['moves'] == 4:
        stars_list['moves'] = 0
        stars_list['list'].pop(0)
    for i in range(len(stars_list['list'])):
        move_star(stars_list['list'][i])


# star1 = create_star(x=123, y=[12, 52], s=[1, 2, 3])
# print(star1)
# move_star(star1)
# print(star1)
# stars_list1 = create_stars_list(20, x=800, y=[0, 600], s=[1, 2, 3])
# print(stars_list1)
# manual_stars_list2 = [create_star(x=10, y=10, s=3),
#                       create_star(x=10, y=20, s=2),
#                create_star(x=10, y=14, s=1)]
# print(manual_stars_list2)
# move_stars(manual_stars_list2)
# print(manual_stars_list2)
# move_stars(manual_stars_list2)
# print(manual_stars_list2)
# move_stars(manual_stars_list2)
# print(manual_stars_list2)
# move_stars(manual_stars_list2)
# print(manual_stars_list2)
stars_list1 = create_stars_list(3, x=800, y=[0, 600], s=[1, 2, 3])
while len(stars_list1['list']) > 0:
    print(stars_list1)
    move_stars(stars_list1)
