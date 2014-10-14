import pygame


class Button(object):
    def __init__(self, name, pos, width, height, color, text, text_color, text_size, text_pos, next_game_state):
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
        self.state = 'up'
        self.next_game_state = next_game_state

    def check_mouse_pos(self, pos):
        if pos[0] >= self.x and pos[0] <= self.x + self.width:
            if pos[1] >= self.y and pos[1] <= self.y + self.height:
                return True
        return False


    def change_button_state(self, pressed, new_state):
        if pressed == True:
            self.state = new_state
            return self.name
        return None


    def draw(self, screen):
        if self.state == 'up':
            self.draw_up(screen)
        else:
            self.draw_down(screen)


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
        new_text_pos = (self.text_pos[0]+3, self.text_pos[1]+3)
        screen.blit(label, new_text_pos)


