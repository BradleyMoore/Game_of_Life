from collections import Counter
import sys

import pygame

from life import Cell


WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode([WIDTH,HEIGHT])

TO_LIVE = [2, 3]
TO_BE_BORN = [3]


def create_life(life, neighbors):
	new_life = []
	neighbor_dict = Counter(neighbors)
	neighbor_list = neighbor_dict.items()

	for pos, count in neighbor_list:
		if count in TO_BE_BORN and pos not in life:
			new_life.append(pos)
		if count in TO_LIVE and pos in life:
			new_life.append(pos)

	return new_life


def draw_game(life):
    for cell in life:
    	cell.draw(SCREEN)


def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


def game_actions(old_life):
	life = []

	neighbors = get_neighbors(old_life)
	new_life = create_life(old_life, neighbors)

	for coordinate in new_life:
	    life.append(Cell(coordinate))

	return life


def get_neighbors(life):
	neighbors = []

	for cell in life:
		neighbors.extend(cell.list_neighbors())

	return neighbors
