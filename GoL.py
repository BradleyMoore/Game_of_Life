import os
import sys
from time import sleep

import pygame

from app.game import draw_game, event_handler, game_actions, SCREEN
from app.life import Pattern


os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

clock = pygame.time.Clock()
fps = 30

init_life = Pattern('block', (0,0))
life = init_life.create_pattern()

while __name__ == '__main__':
    tickFPS = clock.tick(fps)
    pygame.display.set_caption("Press Esc to quit. FPS: %.2f" % (clock.get_fps()))
    SCREEN.fill((0,0,0))
    event_handler()
    draw_game(life)
    life = game_actions()
    pygame.display.flip()
