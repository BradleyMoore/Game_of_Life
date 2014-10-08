import pygame


class Cell(object):

    def __init__(self, pos):
        self.color = (255,0,0)
        self.neighbors = 0
        self.neighbor_list = []
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]


    def draw(self, screen, height, width):
        if self.x < 0 or self.x > width:
            pass
        elif self.y < 0 or self.y > height:
            pass
        else:
            pygame.draw.rect(screen, self.color, (self.x*10, self.y*10, 10, 10))


    def list_neighbors(self):
        self.neighbor_list = []

        for x in xrange(self.x-1, self.x+2):
            for y in xrange(self.y-1, self.y+2):
                self.neighbor_list.append((x,y))

        self.neighbor_list.remove(self.pos)

        return self.neighbor_list


class Pattern(object):

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]


    def create_pattern(self):
        from patterns import patterns

        pattern = patterns[self.name]
        coordinates = []

        for y in xrange(len(pattern)):
            for x in xrange(len(pattern[y])):
                if pattern[y][x] == 1:
                    coordinates.append((self.x+x, self.y+y))

        return coordinates
