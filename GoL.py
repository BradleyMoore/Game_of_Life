import os
import pygame
import sys
from time import sleep
from game_objects import Food, Level, Snake
from game_state import BOX, SCREEN, State


os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

clock = pygame.time.Clock()
fps = 30


def draw_game():
    pass


def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


def game_actions():
	pass


state = State()

while __name__ == '__main__':
    tickFPS = clock.tick(fps)
    pygame.display.set_caption("Press Esc to quit. FPS: %.2f" % (clock.get_fps()))
    SCREEN.fill((0,0,0))
    event_handler()
    draw_game()
    game_actions()
    pygame.display.flip()\
