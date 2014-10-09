import pygame


class Button(object):
    def __init__(self, pos, width, height, color, text, text_color, text_size, text_pos):
        self.x = pos[0]
        self.y = pos[1]
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.text_size = text_size
        self.text_pos = text_pos

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        myfont = pygame.font.SysFont('monospace', self.text_size)
        label = myfont.render(self.text, 1, self.text_color)
        screen.blit(label, self.text_pos)
