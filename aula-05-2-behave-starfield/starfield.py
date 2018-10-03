"""Starfield functions."""

from random import randint, choice


def create_star(y_range, speedlist):
    """Create star function."""
    x = 800
    y = randint(y_range[0], y_range[1])
    speed = choice(speedlist)
    return (x, y, speed)
