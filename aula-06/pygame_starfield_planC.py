#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PyGame screen example."""

# Using Sprites from pygame and coding inside main()

# Módulos
import sys
import pygame
import starfield
import random
from pygame.locals import *

# Constants
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
STAR_COLOR = (255, 255, 255)
STAR_QUANTITY = 20
FRAME_RATE = 420


# Classes
# ---------------------------------------------------------------------
class Starfield(pygame.sprite.Sprite):
    """Test."""

    def __init__(self, color, width, height):
        """Test."""
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

        new_star = starfield.create_star(x=[0, WIDTH],
                                         y=[0, HEIGHT], s=[1, 2, 3])

        self.rect.centerx = new_star['x']
        self.rect.centery = new_star['y']

        self.speed = [-new_star['s'], 0]

    def move_star(self, time):
        """Test."""
        self.rect.centerx += self.speed[0]*time
        if self.rect.centerx == 0:
            self.rect.centerx = WIDTH


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

    starfield_list = []
    for i in range(0, STAR_QUANTITY):
        starfield_list.append(Starfield(STAR_COLOR, random.randint(1, 3),
                                        random.randint(1, 3)))

    moves = 0

    # starship = pygame.Surface([10, 10])
    # starship.fill((125, 250, 123))
    starship = pygame.image.load("images/star_wars_01_s.png")
    speed = [2, 2]
    starship_rect = starship.get_rect()
    starship_rect.centerx = WIDTH / 2
    starship_rect.centery = HEIGHT / 2

    running = True
    while running:
        time = clock.tick(FRAME_RATE)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[K_ESCAPE]:
                sys.exit(0)
                running = False

        if len(starfield_list) == 0:
            for i in range(0, STAR_QUANTITY):
                starfield_list.append(Starfield(STAR_COLOR,
                                                random.randint(1, 3),
                                                random.randint(1, 3)))

        for i in range(0, len(starfield_list)):
            moves += 1
            if moves == 4:
                starfield_list[i].move_star(time)
                starfield_list.pop(0)
                moves = 0
                break
            else:
                starfield_list[i].move_star(time)

        screen.fill(BACKGROUND_COLOR)

        for i in range(0, len(starfield_list)):
            screen.blit(starfield_list[i].image, starfield_list[i].rect)

        screen.blit(starship, starship_rect)
        pygame.display.flip()
    return 0


if __name__ == '__main__':
    pygame.init()
    main()

#
