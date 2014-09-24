import os
import sys
from time import sleep

import pygame

from app.game import draw_game, event_handler, game_actions


WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode([WIDTH,HEIGHT])

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

clock = pygame.time.Clock()
fps = 30


while __name__ == '__main__':
    tickFPS = clock.tick(fps)
    pygame.display.set_caption("Press Esc to quit. FPS: %.2f" % (clock.get_fps()))
    SCREEN.fill((0,0,0))
    event_handler()
    draw_game()
    game_actions()
    pygame.display.flip()
