import os
import sys
from time import sleep

import pygame

from app.game import draw_game, event_handler, game_actions, draw_pause
from app.life import Cell, Pattern
from app.scenes import TitleScene


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
state = 'title'

title = TitleScene(HEIGHT, WIDTH, (50,50,200))

while __name__ == '__main__':
    tickFPS = clock.tick(fps)
    pygame.display.set_caption("Press Esc to quit. FPS: %.2f" % (clock.get_fps()))
    state = event_handler(state)
    if state == 'title':
        title.draw(SCREEN)
    elif state == 'game':
        draw_game(life, SCREEN, HEIGHT, WIDTH)
        old_life = life
        life = game_actions(old_life)
    elif state == 'pause':
        draw_pause(SCREEN, HEIGHT, WIDTH)
    pygame.display.flip()
