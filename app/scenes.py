import pygame

from constants import BOX, HEIGHT, WIDTH, SCREEN
from interactive import Button


class Scene(object):
    def __init__(self, background):
        self.background = background
        self.rects = []
        self.texts = []
        self.lines = []
        self.buttons = {}

    def draw(self, **kwargs):
        SCREEN.fill(self.background)

        if 'life' in kwargs:
            for cell in kwargs['life']:
                cell.draw()

        for rect in self.rects:
            pygame.draw.rect(SCREEN, rect['color'], (rect['x'],rect['y'],rect['WIDTH'],rect['HEIGHT']), rect['stroke'])

        for line in self.lines:
            pygame.draw.line(SCREEN, line['color'], (line['startx'],line['starty']), (line['endx'],line['endy']), line['width'])


        for text in self.texts:
            SCREEN.blit(text[0], (text[1]))

        button_list = self.buttons.keys()
        for button in button_list:
            self.buttons[button].draw_up(SCREEN)


class TitleScene(Scene):
    def __init__(self, background):
        Scene.__init__(self, background)

        # start button
        self.buttons['start'] = (Button('start', (WIDTH*.65,HEIGHT*.67),
                                WIDTH*.1, HEIGHT*.1, (200,200,200),
                                'START', (100,100,100,), 40,
                                (WIDTH*.655, HEIGHT*.69)))

        # black matte
        self.rects.append({'color': (0,0,0), 'x': 0, 'y': 0, 'WIDTH': WIDTH, 'HEIGHT': HEIGHT, 'stroke': HEIGHT/9})
        # red border
        self.rects.append({'color': (200,50,50), 'x': 0, 'y': 0, 'WIDTH': WIDTH, 'HEIGHT': HEIGHT, 'stroke': HEIGHT/10})

        # title
        myfont = pygame.font.SysFont('monospace', 200)
        self.texts.append((myfont.render("Conway's", 1, (255,255,0)),(200,50)))
        self.texts.append((myfont.render('Game of', 1, (255,255,0)),(250,250)))
        self.texts.append((myfont.render('LIFE', 1, (255,255,0)),(300,450)))


class GameScene(Scene):
    def __init__(self, background):
        Scene.__init__(self, background)

        for i in xrange(0, WIDTH, BOX):
            self.lines.append({'color': (100,100,100), 'startx': i, 'starty': 0, 'endx': i, 'endy': HEIGHT, 'width': 1})
        for i in xrange(0, HEIGHT, BOX):
            self.lines.append({'color': (100,100,100), 'startx': 0, 'starty': i, 'endx': WIDTH, 'endy': i, 'width': 1})

        # start button
        self.buttons['pause'] = (Button('pause', (WIDTH*.75,HEIGHT*.75),
                                WIDTH*.07, HEIGHT*.07, (200,200,200),
                                'PAUSE', (100,100,100,), 28,
                                (WIDTH*.752, HEIGHT*.765)))

        self.buttons['play'] = (Button('play', (WIDTH*.825,HEIGHT*.75),
                                WIDTH*.07, HEIGHT*.07, (200,200,200),
                                'PLAY', (100,100,100,), 28,
                                (WIDTH*.833, HEIGHT*.765)))
