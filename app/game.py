import sys

import pygame

from interactive import Button
from life import Cell, create_life, get_neighbors
from scenes import GameScene, TitleScene
from constants import HEIGHT, WIDTH, SCREEN

# game rules
TO_LIVE = [2, 3]
TO_BE_BORN = [3]

title = TitleScene((50,50,200))
game = GameScene((150,150,150))

states = {}
states['title'] = title
states['game'] = game


def draw_pause(screen, height, width):
    pygame.draw.rect(screen, (255,0,255), (900,550,100,50))
    myfont = pygame.font.SysFont('monospace', 20)
    label = myfont.render('RESUME', 1, (255,255,0))
    screen.blit(label, (920, 560))


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
        name = states[state].check_buttons(pos, 'down')
        if name != None:
            states[state].buttons[name].state = 'down'

    elif event.type == pygame.MOUSEBUTTONUP:
        states[state].set_buttons_up()
        pos = pygame.mouse.get_pos()
        name = states[state].check_buttons(pos, 'up')
        if name != None:
            return states[state].buttons[name].next_game_state


def game_actions(old_life):
	life = []

	neighbors = get_neighbors(old_life)
	new_life = create_life(old_life, neighbors)

	for coordinate in new_life:
	    life.append(Cell(coordinate))

	return life
