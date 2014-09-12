from __future__ import print_function
import sys


class Board(object):
    def __init__(self, hsize, vsize):
        self.hsize = hsize
        self.vsize = vsize
        self.board = []

    def create(self):
        self.board = [[0 for j in xrange(self.hsize)] for i in xrange(self.vsize)]

    def show(self):
        for i in xrange(self.vsize):
            for j in xrange(self.hsize):
                print(self.board[i][j], end='')
            print('', end='\n')

