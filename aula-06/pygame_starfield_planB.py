#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Starfield - plan B - PyGame screen."""

# Using starfield module functions mixed with Starfield class

# Modules
import sys
import pygame
import starfield
import random
from pygame.locals import K_ESCAPE

# Constants
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
STARS_COLOR = (255, 255, 255)
STARS_AMOUNT = 20
STARS_RANGE_SIZE = [1, 3]
FRAME_RATE = 120


# Classes
# ---------------------------------------------------------------------
class MainStarship(object):
    """Main ship class."""

    def __init__(self):
        """Initialize Main Starship."""
        self.image = pygame.image.load('images/star_wars_01_s.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2


# class Star(object):
#     """Star class."""
#
#     def __init__(self, color, width, height, x, y, s):
#         """Initialize Star."""
#         self.image = pygame.Surface([width, height])
#         self.image.fill(color)
#         self.rect = self.image.get_rect()
#         self.star = starfield.create_star(x=x, y=y, s=s)
#
#         self.x = self.star['x']
#
#         self.rect.centerx = self.star['x']
#         self.rect.centery = self.star['y']
#
#         self.speed = [-self.star['s'], 0]


class Starfield(object):
    """Starfield class."""

    def __init__(self, stars_amount, stars_color, width, height):
        """Initialize Starfield."""
        w = width
        h = height
        self.stars = starfield.create_stars_list(stars_amount, x=[0, WIDTH],
                                                 y=[0, HEIGHT], s=[1, 2, 3])

        self.starlist = self.stars['list']

        self.image = []
        self.rect = []
        self.speed = []

        for i in range(0, len(self.starlist)):
            self.image.append(pygame.Surface([random.randint(w[0], w[1]),
                                             random.randint(h[0], h[1])]))
            self.image[i].fill(stars_color)
            self.rect.append(self.image[i].get_rect())
            self.rect[i].centerx = self.starlist[i]['x']
            self.rect[i].centery = self.starlist[i]['y']
            self.speed.append([-self.starlist[i]['s'], 0])

    def move(self, time):
        """Move the stars."""
        if len(self.starlist) > 0:
            print("move")
            starfield.move_stars(self.stars)
            for i in range(0, len(self.starlist)):
                self.rect[i].centerx += -self.starlist[i]['s']  # * time


# ---------------------------------------------------------------------

# Functions
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------


def main():
    """Run the game."""
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Space Wars')
    screen.fill(BACKGROUND_COLOR)

    starfield_bg = Starfield(STARS_AMOUNT, STARS_COLOR, STARS_RANGE_SIZE,
                             STARS_RANGE_SIZE)

    main_starship = MainStarship()

    running = True
    while running:
        time = clock.tick(FRAME_RATE)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[K_ESCAPE]:
                sys.exit(0)
                running = False

        screen.fill(BACKGROUND_COLOR)

        if len(starfield_bg.starlist) == 0:
            starfield_bg = Starfield(STARS_AMOUNT, STARS_COLOR,
                                     STARS_RANGE_SIZE,
                                     STARS_RANGE_SIZE)

        for i in range(len(starfield_bg.starlist)):
            screen.blit(starfield_bg.image[i], starfield_bg.rect[i])
            # print("estrela {}: x= {}, s={}".format(i, starfield_bg.rect[i].
            # centerx, starfield_bg.speed[i]))

        starfield_bg.move(time)
        print("flip")
        print(len(starfield_bg.starlist))

        # screen.blit(star.image, star.rect)
        # print(starfield.image)
        screen.blit(main_starship.image, main_starship.rect)
        pygame.display.flip()
    return 0


if __name__ == '__main__':
    pygame.init()
    main()

#
