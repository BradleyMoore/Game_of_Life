from collections import Counter

import pygame

from constants import BOX, HEIGHT, WIDTH, SCREEN
 

class Cell(object):

    def __init__(self, pos):
        self.color = (255,0,0)
        self.neighbors = 0
        self.neighbor_list = []
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]


    def draw(self):
        if self.x < 0 or self.x > WIDTH:
            pass
        elif self.y < 0 or self.y > HEIGHT:
            pass
        else:
            pygame.draw.rect(SCREEN, self.color, (self.x*BOX, self.y*BOX, BOX, BOX))


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


def create_life(life, neighbors):
    from game import TO_BE_BORN, TO_LIVE
    new_life = []
    # turn neighbor positions into a list of tuples
    neighbor_dict = Counter(neighbors)
    neighbor_list = neighbor_dict.items()

    life_pos = []
    for cell in life:
        life_pos.append(cell.pos)

    for pos, count in neighbor_list:
        # give birth to cells
        if count in TO_BE_BORN and pos not in life_pos:
            new_life.append(pos)
        # cells staying alive
        if count in TO_LIVE and pos in life_pos:
            new_life.append(pos)

    return new_life


def get_neighbors(life):
    neighbors = []

    for cell in life:
        neighbors.extend(cell.list_neighbors())

    return neighbors
