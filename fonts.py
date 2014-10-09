import os
import sys
from time import sleep

import pygame


pygame.init()
pygame.display.init()

modes = pygame.display.list_modes()

WIDTH = modes[0][0]
HEIGHT = modes[0][1]
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)

clock = pygame.time.Clock()
fps = 15

fonts = pygame.font.get_fonts()

while __name__ == '__main__':
    tickFPS = clock.tick(fps)
    pygame.display.set_caption("Press Esc to quit. FPS: %.2f" % (clock.get_fps()))

    SCREEN.fill((0,0,0))
    i = 10
    j = 0
    k = 10
    for font in fonts:
        myfont = pygame.font.SysFont(font, 15)
        label = myfont.render(font, 1, (255,255,255))
        SCREEN.blit(label, (k, i))
        i = i + 25
        j = j + 1
        if j % 40 == 0:
            k = k + 250
            i = 10
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    pygame.display.flip()
