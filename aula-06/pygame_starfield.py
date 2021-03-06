#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Starfield - PyGame screen."""

# Using only Starfield class methods (derived with modifications from starfield
# method)

# Módulos
import sys
import pygame
# import starfield
import random
# from pygame.locals import K_ESCAPE

# Constants
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
STAR_COLOR = (255, 255, 255)
STARS_AMOUNT = 20
STAR_SIZES = [1, 3]
FRAME_RATE = 60


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


class Starfield(object):
    """Starfield class."""

    def __init__(self, stars_amount, stars_color, star_sizes, screen):
        """Initialize Starfield."""
        self.stars_amount = stars_amount
        self.stars_color = stars_color
        self.star_sizes = star_sizes
        self.stars = self.create_stars_list(stars_amount, x=[0, WIDTH],
                                            y=[0, HEIGHT], s=[1, 2, 3],
                                            t=[1, 3])
        # returns a dictionary

        self.starlist = self.stars['list']
        self.moves = self.stars['moves']

        self.screen = screen

        # print(self.starlist[0])

    def get_list(self):
        """."""
        return self.starlist

    def create_star(self, **kwargs):
        """Create a star given X (X range), Y (Y range) and speed list."""
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

        if type(kwargs['t']) == int:
            t = kwargs['t']
        else:
            t = random.choice(kwargs['t'])

        return {'x': x, 'y': y, 's': s, 't': t}

    def create_stars_list(self, quantity, **kwargs):
        """Create a list of stars."""
        index = 0
        moves = 0
        stars_list = []
        while index < quantity:
            stars_list.append(self.create_star(**kwargs))
            index += 1
        return {'list': stars_list, 'moves': moves}

    # TODO: ALTERAR PARA CRIAR UMA LISAT DE ESTRELAS POR FORA? oU POR DENTRO DA
    # CLASSE, MAS QUE NÃO FIQUEM VARIANDO DE TAMANHO SE PARADAS
    # oU QUANDO SE MOVER VAI SER INTERESSANTE FICAR DESENHANDO SEMPRE ESTA
    # LISta

    def _draw(self, i):
        """."""
        pygame.draw.rect(self.screen, STAR_COLOR, [self.starlist[i]['x'],
                         self.starlist[i]['y'], self.starlist[i]['t'],
                         self.starlist[i]['t']], 0)

    def draw_list(self):
        """."""
        for i in range(len(self.starlist)):
            self._draw(i)

    def move_star(self, star):
        """Move a star."""
        star['x'] -= star['s']

    def move_stars(self, time):
        """Move all the stars given a dictionary of stars {'moves', 'list'}."""
        """And delete the first star every 4 moves."""
        list_length = len(self.starlist)
        self.moves += 1
        moves = self.moves
        if moves == 4:
            self.moves = 0
            if list_length > 0:
                self.starlist.pop(0)
                list_length -= 1
        if list_length > 0:
            for i in range(list_length):
                self.move_star(self.starlist[i])
        if list_length < STARS_AMOUNT:  # recria estrelas
            self.starlist.append(self.create_star(x=[0, WIDTH],
                                 y=[0, HEIGHT], s=[1, 2, 3], t=[1, 3]))

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

    starfield_bg = Starfield(STARS_AMOUNT, STAR_COLOR, STAR_SIZES, screen)

    # sl = starfield_bg.get_list()
    # print(sl[1]['x'])

    main_starship = MainStarship()

    running = True
    while running:
        time = clock.tick(FRAME_RATE)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                sys.exit(0)
                running = False

        screen.fill(BACKGROUND_COLOR)

        # if len(starfield_bg.starlist) == 0:
        #     starfield_bg = Starfield(STARS_AMOUNT, STAR_COLOR,
        #                              STAR_SIZES,
        #                              STAR_SIZES, screen)

        # starfield_bg.move_stars(time)

        starfield_bg.draw_list()
        starfield_bg.move_stars(time)

        screen.blit(main_starship.image, main_starship.rect)
        pygame.display.flip()
    return 0


if __name__ == '__main__':
    pygame.init()
    main()

#
