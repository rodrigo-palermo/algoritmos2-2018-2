"""Verify wheter two rectangles collide with each other."""


rectangle1 = {'x': 0, 'y': 0, 'width': 3, 'height': 4}
rectangle2 = {'x': 0, 'y': 0, 'width': 3, 'height': 4}
# width: x to right,
# height: y to up


def is_point_inside(a_point, a_rectangle):
    """Verify whether a point is inside of a rectangle."""
    if a_point['x'] >= a_rectangle['x'] and \
       a_point['x'] <= (a_rectangle['x'] + a_rectangle['width']) and \
       a_point['y'] >= a_rectangle['y'] and \
       a_point['y'] <= (a_rectangle['y'] + a_rectangle['height']):
        return True
    else:
        return False


def is_collided(rect1, rect2):
    """Verify whether a rectangle collides with another one."""
    if is_point_inside(get_corner_point(rect1, 1), rect2):
        return True
    elif is_point_inside(get_corner_point(rect1, 2), rect2):
        return True
    elif is_point_inside(get_corner_point(rect1, 3), rect2):
        return True
    elif is_point_inside(get_corner_point(rect1, 4), rect2):
        return True
    else:
        return False


def get_corner_point(rect, corner):
    """From origin, clockwise."""
    if corner == 1:
        coord_x = rect.get('x')
        coord_y = rect.get('y')
    elif corner == 2:
        coord_x = rect.get('x')
        coord_y = rect.get('y') + rect.get('height')
    elif corner == 3:
        coord_x = rect.get('x') + rect.get('width')
        coord_y = rect.get('y') + rect.get('height')
    else:
        coord_x = rect.get('x') + rect.get('width')
        coord_y = rect.get('y')

    corner_point = {'x': coord_x, 'y': coord_y}
    return corner_point


print(get_corner_point(rectangle1, 1))
print(get_corner_point(rectangle1, 2))
print(get_corner_point(rectangle1, 3))
print(get_corner_point(rectangle1, 4))

print("Collided: %s" % is_collided(rectangle1, rectangle2))

print(is_collided(rectangle1, rectangle2))
