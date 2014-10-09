import pygame

from interactive import Button


class Scene(object):
    def __init__(self, height, width, background):
        self.height = height
        self.width = width
        self.background = background
        self.items = []
        self.texts = []
        self.buttons = []

    def draw(self, screen):
        screen.fill(self.background)

        for item in self.items:
            pygame.draw.rect(screen, item['color'], (item['x'],item['y'],item['width'],item['height']), item['stroke'])

        for text in self.texts:
            screen.blit(text[0], (text[1]))

        for button in self.buttons:
            button.draw(screen)


class TitleScene(Scene):
    def __init__(self, height, width, background):
        Scene.__init__(self, height, width, background)

        # start button
        self.buttons.append(Button((self.width*.65,self.height*.67),
                            self.width*.1, self.height*.1, (255,0,255),
                            'START', (255,255,0), 20,
                            (self.width*.675, self.height*.70)))

        # matte black
        self.items.append({'color': (0,0,0), 'x': 0, 'y': 0, 'width': self.width, 'height': self.height, 'stroke': self.height/9})
        # red border
        self.items.append({'color': (200,50,50), 'x': 0, 'y': 0, 'width': self.width, 'height': self.height, 'stroke': self.height/10})

        # title
        myfont = pygame.font.SysFont('monospace', 200)
        self.texts.append((myfont.render("Conway's", 1, (255,255,0)),(200,50)))
        self.texts.append((myfont.render('Game of', 1, (255,255,0)),(250,250)))
        self.texts.append((myfont.render('LIFE', 1, (255,255,0)),(300,450)))
