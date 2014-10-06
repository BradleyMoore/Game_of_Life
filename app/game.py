from collections import Counter
import sys

import pygame

from life import Cell


TO_LIVE = [2, 3]
TO_BE_BORN = [3]


def create_life(life, neighbors):
	new_life = []
	neighbor_dict = Counter(neighbors)
	neighbor_list = neighbor_dict.items()

	life_pos = []
	for cell in life:
		life_pos.append(cell.pos)

	for pos, count in neighbor_list:
		if count in TO_BE_BORN and pos not in life_pos:
			new_life.append(pos)
		if count in TO_LIVE and pos in life_pos:
			new_life.append(pos)

	return new_life


def draw_game(life, screen):
    for cell in life:
    	cell.draw(screen)


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
