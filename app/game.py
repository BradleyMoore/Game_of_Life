import pygame

from interactive import Button
from life import Cell, create_life, get_neighbors
from scenes import TitleScene


pygame.init()
pygame.display.init()

modes = pygame.display.list_modes()

WIDTH = modes[0][0]
HEIGHT = modes[0][1]
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)

# game rules
TO_LIVE = [2, 3]
TO_BE_BORN = [3]

title = TitleScene(HEIGHT, WIDTH, (50,50,200))

states = {}
states['title'] = title.draw(SCREEN)


def draw_game(life, screen, height, width):
    # draw game board
    screen.fill((0,0,0))

    # draw pause button
    pygame.draw.rect(screen, (255,0,255), (900,550,100,50))
    myfont = pygame.font.SysFont('monospace', 20)
    label = myfont.render('PAUSE', 1, (255,255,0))
    screen.blit(label, (920, 560))

    # draw cells
    for cell in life:
        cell.draw(screen, height, width)


def draw_pause(screen, height, width):
    pygame.draw.rect(screen, (255,0,255), (900,550,100,50))
    myfont = pygame.font.SysFont('monospace', 20)
    label = myfont.render('RESUME', 1, (255,255,0))
    screen.blit(label, (920, 560))


def event_handler(state):
    from game import SCREEN
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        elif state == 'title':
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pressed = title.buttons['start'].check_mouse_pos(pos)
                if pressed == True:
                    title.buttons['start'].draw_down(SCREEN)
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                # check if start is clicked
                if pos[0] > 900 and pos[0] < 1000:
                    if pos[1] > 550 and pos[1] < 600:
                        return 'game'

        elif state == 'game':
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] > 900 and pos[0] < 1000:
                    if pos[1] > 550 and pos[1] < 600:
                        return 'pause'

        elif state == 'pause':
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] > 900 and pos[0] < 1000:
                    if pos[1] > 550 and pos[1] < 600:
                        return 'game'

            return 'pause'

    return state


def game_actions(old_life):
	life = []

	neighbors = get_neighbors(old_life)
	new_life = create_life(old_life, neighbors)

	for coordinate in new_life:
	    life.append(Cell(coordinate))

	return life
