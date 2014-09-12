from config import HSIZE, VSIZE, NEIGHBORS_FOR_BIRTH, NEIGHBORS_FOR_LIFE
from app.cells import Cell


def let_there_be_life(hsize, vsize, birth_neighbors, life_neighbors):
    life = [[None for j in xrange(vsize)] for i in xrange(hsize)]
    for i in xrange(vsize):
        for j in xrange(hsize):
            life[j][i] = (Cell(j, i, birth_neighbors, life_neighbors))

    return life


life = let_there_be_life(HSIZE, VSIZE, NEIGHBORS_FOR_BIRTH, NEIGHBORS_FOR_LIFE)
print life


while __name__ == '__main__':
    break

