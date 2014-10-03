import os
import sys
from time import sleep

import pygame

from app.game import draw_game, event_handler, game_actions, SCREEN
from app.life import Cell, Pattern


os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

clock = pygame.time.Clock()
fps = 1

life = []
init_life = Pattern('pulsar', (150,150))
coordinate_list = init_life.create_pattern()
for coordinate in coordinate_list:
    life.append(Cell(coordinate))

old_life = []

while __name__ == '__main__':
    tickFPS = clock.tick(fps)
    pygame.display.set_caption("Press Esc to quit. FPS: %.2f" % (clock.get_fps()))
    SCREEN.fill((0,0,0))
    event_handler()
    draw_game(life)
    old_life = life
    life = game_actions(old_life)
    pygame.display.flip()
