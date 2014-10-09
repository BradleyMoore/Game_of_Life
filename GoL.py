import os
import sys
from time import sleep

import pygame

from app.game import draw_game, event_handler, game_actions, draw_pause, HEIGHT, WIDTH, SCREEN
from app.life import Cell, Pattern
from app.scenes import TitleScene


clock = pygame.time.Clock()
fps = 15

life = []
init_life = Pattern('r-pentomino', (60,40))
coordinate_list = init_life.create_pattern()
for coordinate in coordinate_list:
    life.append(Cell(coordinate))


old_life = []
state = 'game'

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
