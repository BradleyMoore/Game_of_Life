import sys

import pygame

from constants import BOX, HEIGHT, WIDTH, SCREEN, TO_BE_BORN, TO_LIVE


class Game(object):
    def __init__(self):
        self.fps = 11


    def do_action(self, action):
        if action == 'slow_down':
            self.change_game_speed(.9)
        elif action == 'normal_speed':
            self.set_normal_speed()
        elif action == 'speed_up':
            self.change_game_speed(1.11)
        elif action == 'zoom_out':
            self.box = self.box*.9
        elif action == 'zoom_in':
            self.box = self.box*1.11


    def change_game_speed(self, change):
        self.fps = self.fps * change
        if self.fps < 1:
            self.fps = 1
        if self.fps > 100:
            self.fps = 100


    def set_normal_speed(self):
        self.fps = 11


    def game_actions(self, old_life):
        life = []

        neighbors = get_neighbors(old_life)
        new_life = create_life(old_life, neighbors)

        for coordinate in new_life:
            life.append(Cell(coordinate))

        return life


gamestate = Game()

from life import Cell, create_life, get_neighbors
from scenes import GameScene, TitleScene

title = TitleScene((50,50,200))
game = GameScene((150,150,150))
pause = GameScene((150,150,150))
exit = GameScene((150,150,150))

states = {}
states['title'] = title
states['game'] = game
states['pause'] = pause
states['exit'] = exit


def event_handler(state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        elif event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN:
            next_game_state = click_buttons(event, state)
            if next_game_state != None:
                return next_game_state

    return state


def click_buttons(event, state):
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        name, action = states[state].check_buttons(pos, 'down')
        if name != None:
            states[state].buttons[name].state = 'down'

    elif event.type == pygame.MOUSEBUTTONUP:
        states[state].set_buttons_up()
        pos = pygame.mouse.get_pos()
        name, action = states[state].check_buttons(pos, 'up')
        if name != None:
            if action != None:
                gamestate.do_action(action)
            if name != state:
                return states[state].buttons[name].next_game_state
            else:
                return None
