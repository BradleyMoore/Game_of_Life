from collections import Counter
import sys

import pygame


WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode([WIDTH,HEIGHT])

TO_LIVE = [2, 3]
TO_BE_BORN = [3]


def actions(life):
	new_life = []
	neighbors = []

	neighbors = get_neighbors(life)
	new_life = create_life(neighbors)

	return new_life


def create_life(neighbors):
	life = []
	neighbor_dict = Counter(neighbors)
	neighbor_list = neighbordict.items()

	for pos, count in neighbor_list:
		if count in TO_LIVE or count in TO_BE_BORN:
			life.append(pos)

	return life


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
	neighbors = get_neighbors(old_life)
	life = create_life(neighbors)

	return life


def get_neighbors(life):
	neighbors = []

	for cell in all_possible_neighbors:
		neighbors.extend(cell.list_neighbors())

	return neighbors
