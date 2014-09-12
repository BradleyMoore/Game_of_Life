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
possible_neighbors = []


while __name__ == '__main__':
    for i in xrange(VSIZE):
        for j in xrange(HSIZE):
            cell = life[j][i]
            possible_neighbors = []

            possible_neighbors = cell.find_neighbors(HSIZE, VSIZE)

            for neighbor in possible_neighbors:
                cell.check_neighbor(life[neighbor[0]][neighbor[1]])

            cell.reap_and_sew()

            if cell.status == 0:
                print(' ', end='')
            else:
                print('O', end='')
        print('\n')
    os.system('clear')

