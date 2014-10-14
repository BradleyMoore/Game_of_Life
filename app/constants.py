import pygame


pygame.init()
pygame.display.init()

modes = pygame.display.list_modes()

WIDTH = modes[0][0]
HEIGHT = modes[0][1]
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)

BOX = WIDTH/200

# game rules
TO_LIVE = [2, 3]
TO_BE_BORN = [3]
