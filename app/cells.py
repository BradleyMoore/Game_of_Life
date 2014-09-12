class Cell(object):
    def __init__(self, xpos, ypos, numtobirth, numtolive):
        self.neighbors = 0
        self.numtobirth = numtobirth
        self.numtolive = numtolive
        self.status = ''
        self.xpos = xpos
        self.ypos = ypos
        self.pos = [self.xpos, self.ypos]

    def count_neighbors(self, live_board):


    def create(self, neighbors):
        if self.status == 'dead'
            if neighbors in self.numtobirth:
                self.status = 'alive'

    def destroy(self, neighbors):
        if self.status == 'alive':
            if neighbors not in self.numtolive:
                self.status = 'dead'

