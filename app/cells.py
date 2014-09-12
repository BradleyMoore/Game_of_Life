class Cell(object):

    def __init__(self, xpos, ypos, numtobirth, numtolive):
        self.neighbors = 0
        self.numtobirth = numtobirth
        self.numtolive = numtolive
        self.status = ''
        self.xpos = xpos
        self.ypos = ypos
        self.pos = (xpos, ypos)

    def check_neighbors(self, xpos, ypos):
        if life[xpos][ypos].satus == 1:
            self.neighbors = self.neighbors + 1

    '''
    def count_neighbors(self, live_board):
        if self.ypos != 0:
            
            if self.xpos != 0:
                '''


    def be_born(self, neighbors):
        if self.status == 0:
            if neighbors in self.numtobirth:
                self.status = 1

    def die(self, neighbors):
        if self.status == 1: 
            if neighbors not in self.numtolive:
                self.status = 0

