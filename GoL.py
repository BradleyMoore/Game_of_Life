import os
import sys
from time import sleep

import pygame

from app.constants import HEIGHT, WIDTH, SCREEN
from app.game import event_handler, gamestate, game, pause, title
from app.life import Cell, Pattern


clock = pygame.time.Clock()

life = []

old_life = []
state = 'title'

while __name__ == '__main__':
    tickFPS = clock.tick(gamestate.fps)

    state = event_handler(state)
    if state == 'title':
        title.draw()
    elif state == 'game':
        life.extend(gamestate.new_pattern)
        gamestate.new_pattern = ''
        game.draw(life=life)
        old_life = life
        life = gamestate.game_actions(old_life)
    elif state == 'pause':
        pause.draw(life=life)
    elif state == 'exit':
        pygame.quit()
        sys.exit()

    pygame.display.flip()
