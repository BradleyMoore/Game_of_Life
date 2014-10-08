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


def draw_game(life, screen, height, width):
	screen.fill((0,0,0))
	for cell in life:
		cell.draw(screen, height, width)


def draw_title_screen(screen, height, width):
	screen.fill((50,50,200))
	pygame.draw.rect(screen, (0,0,0,0,), (0,0,width,height), height/9)
	pygame.draw.rect(screen, (200,50,50), (0,0,width,height), height/10)
	
	myfont = pygame.font.SysFont('monospace', 200)
	label = myfont.render("Conway's", 1, (255,255,0))
	screen.blit(label, (200, 50))
	label = myfont.render('Game of', 1, (255,255,0))
	screen.blit(label, (250, 250))
	label = myfont.render('LIFE', 1, (255,255,0))
	screen.blit(label, (300, 450))

	pygame.draw.rect(screen, (255,0,255), (900,550,100,50))
	myfont = pygame.font.SysFont('monospace', 20)
	label = myfont.render('START', 1, (255,255,0))
	screen.blit(label, (920, 560))


def game_event_handler():
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
