import pygame


class Button(object):
    def __init__(self, name, pos, width, height, color, text, text_color, text_size, text_pos):
        from game import SCREEN
        self.name = name
        self.x = pos[0]
        self.y = pos[1]
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.text_size = text_size
        self.text_pos = text_pos

    def check_mouse_pos(pos):
        if pos[0] >= self.pos[0] and pos[0] <= self.pos[0] + self.width:
            if pos[1] >= self.pos[1] and pos[1] <= self.pos[1] + self.height:
                return true


    def draw_up(self, screen):
        # dark lines
        pygame.draw.rect(screen, (50,50,50), (self.x, self.y, self.width, self.height))
        # white lines
        pygame.draw.rect(screen, (255,255,255), (self.x, self.y, self.width-3, 3))
        pygame.draw.rect(screen, (255,255,255), (self.x, self.y, 3, self.height-3)) 
        # light gray lines
        pygame.draw.rect(screen, (150,150,150), (self.x+3, self.y+3, self.width-6, self.height-6))

        # main button section
        pygame.draw.rect(screen, self.color, (self.x+3, self.y+3, self.width-9, self.height-9))      

        # button text
        myfont = pygame.font.SysFont('lucidaconsole', self.text_size)
        label = myfont.render(self.text, 1, self.text_color)
        screen.blit(label, self.text_pos)


    def draw_down(self, screen):
        # dark lines
        pygame.draw.rect(screen, (255,255,255), (self.x, self.y, self.width, self.height))
        # white lines
        pygame.draw.rect(screen, (50,50,50), (self.x, self.y, self.width-3, 3))
        pygame.draw.rect(screen, (50,50,50), (self.x, self.y, 3, self.height-3)) 
        # light gray lines
        pygame.draw.rect(screen, (150,150,150), (self.x+3, self.y+3, self.width-6, self.height-6))

        # main button section
        pygame.draw.rect(screen, self.color, (self.x+6, self.y+6, self.width-9, self.height-9))      

        # button text
        myfont = pygame.font.SysFont('lucidaconsole', self.text_size)
        label = myfont.render(self.text, 1, self.text_color)
        screen.blit(label, self.text_pos)
