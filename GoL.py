from __future__ import print_function
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

    living_cells = []
    neighbors = []

    for location in living_cells:
        x, y = location
        cell = life[x][y]
        neighbors.extend(cell.find_neighbors(HSIZE, VSIZE))
        
    for location in set(neighbors):
        x, y = location
        cell = life[x][y]
        cell.reap_and_sow()

    for i in xrange(VSIZE):
        for j in xrange(HSIZE):
            cell = life[j][i]
            if cell.status == 0:
                print(' ', end='')
            else:
                print('O', end='')
            print('\n')
    os.system('clear')

