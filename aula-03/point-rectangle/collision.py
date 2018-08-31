"""Verify the collision of a point and a rectangle."""

"""
Both point and rectangle are defined using dictionary, as following
    point = {'x': 0, 'y': 3}
    rectangle = {'x': 0, 'y': 0, 'width': 3, 'height': 4} # width: x to right,
                                                          # height: y to up
"""


def is_point_in_rectangle(a_point, a_rectangle):
    """Verify whether a point is inside of a rectangle."""
    if a_point['x'] >= a_rectangle['x'] and \
       a_point['x'] <= (a_rectangle['x'] + a_rectangle['width']) and \
       a_point['y'] >= a_rectangle['y'] and \
       a_point['y'] <= (a_rectangle['y'] + a_rectangle['height']):
        return True
    else:
        return False

# print(is_point_in_rectangle(point, rectangle))
