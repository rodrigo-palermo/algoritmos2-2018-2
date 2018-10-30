#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Moving point as sprie surface with pygame."""

# Modules
import sys
import pygame
from pygame.locals import K_ESCAPE

# Constants
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
STAR_COLOR = (255, 255, 255)


# Classes
# ---------------------------------------------------------------------
class Star(pygame.sprite.Sprite):
    """Test."""

    def __init__(self, color, width, height):
        """Test."""
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2

        self.speed = [0.5, -0.5]

    def move_star(self):
        """Test."""
        self.rect.centerx += self.speed[0]*6
        self.rect.centery += self.speed[1]*6
        if self.rect.centerx >= WIDTH or self.rect.centerx <= 0:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0]*6
        if self.rect.centery >= HEIGHT or self.rect.centery <= 0:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1]*6

# ---------------------------------------------------------------------

# Functions
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------


def main():
    """Run the game."""
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Hello World')
    screen.fill(BACKGROUND_COLOR)

    star = Star(STAR_COLOR, 10, 10)

    running = True
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[K_ESCAPE]:
                sys.exit(0)
                running = False

        star.move_star()

        screen.fill(BACKGROUND_COLOR)

        screen.blit(star.image, star.rect)

        pygame.display.flip()
    return 0


if __name__ == '__main__':
    pygame.init()
    main()

#
