from __future__ import print_function
import random
import os

from config import HSIZE, VSIZE, NEIGHBORS_FOR_BIRTH, NEIGHBORS_FOR_LIFE
from app.cells import Cell


def let_there_be_life(hsize, vsize, birth_neighbors, life_neighbors):
    life = [[None for j in xrange(vsize)] for i in xrange(hsize)]
    for i in xrange(vsize):
        for j in xrange(hsize):
            life[j][i] = (Cell(j, i, birth_neighbors, life_neighbors))

    return life


life = let_there_be_life(HSIZE, VSIZE, NEIGHBORS_FOR_BIRTH, NEIGHBORS_FOR_LIFE)

for i in xrange(300):
    cell = life[random.randint(0, HSIZE-1)][random.randint(0, VSIZE-1)]
    cell.status = 1

def find_life():

    living_cells = []
    for i in xrange(VSIZE):
        for j in xrange(HSIZE):
            cell = life[j][i]
            if cell.status == 1:
                living_cells.append(cell.pos)

    return living_cells


possible_neighbors = []
living_cells = find_life()

while __name__ == '__main__':

    neighbors = []
    next_round_life = []

    for location in living_cells:
        x, y = location
        cell = life[x][y]
        neighbors.extend(cell.find_neighbors(HSIZE, VSIZE))

    for location in set(neighbors):
        x, y = location
        cell = life[x][y]
        cell.reap_and_sow()
        if cell.status == 1:
            next_round_life.append(cell.pos)

    for location in living_cells:
        x, y = location
        cell = life[x][y]
        print(cell.status)
        cell.reap_and_sow()
        print(cell.status)
        print('\n')
        if cell.status == 1:
            next_round_life.append(cell.pos)

    for i in xrange(VSIZE):
        for j in xrange(HSIZE):
            cell = life[j][i]
            if cell.status == 0:
                print(' ', end='')
            else:
                print('O', end='')
        print('\n')
    for i in xrange(80):
        print('O', end='')
    #os.system('clear')

    living_cells = []
    living_cells = next_round_life
    next_round_life = []
