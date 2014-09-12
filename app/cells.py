class Cell(object):
    def __init__(self):
        self.neighbors = 0
        self.numtobirth = (3)
        self.numtolive = (2, 3)
        self.status = ''

    def count_neighbors(self, live_board):


    def create(self, neighbors):
        if self.status == 'dead'
            if neighbors in self.numtobirth:
                self.status = 'alive'

    def destroy(self, neighbors):
        if self.status == 'alive':
            if neighbors not in self.numtolive:
                self.status = 'dead'

