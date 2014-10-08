import os
import sys
from time import sleep

import pygame

from app.game import draw_game, event_handler, game_actions
from app.life import Cell, Pattern


pygame.init()
pygame.display.init()

modes = pygame.display.list_modes()

WIDTH = modes[0][0]
HEIGHT = modes[0][1]
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)

clock = pygame.time.Clock()
fps = 15

life = []
init_life = Pattern('r-pentomino', (60,40))
coordinate_list = init_life.create_pattern()
for coordinate in coordinate_list:
    life.append(Cell(coordinate))


old_life = []

while __name__ == '__main__':
    tickFPS = clock.tick(fps)
    pygame.display.set_caption("Press Esc to quit. FPS: %.2f" % (clock.get_fps()))
    SCREEN.fill((0,0,0))
    event_handler()
    draw_game(life, SCREEN, HEIGHT, WIDTH)
    old_life = life
    life = game_actions(old_life)
    pygame.display.flip()
