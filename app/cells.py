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


    def find_neighbors(self):
        if self.xpos != 0:
            check_neighbors(self.xpos-1, self.ypos)
            if self.ypos != 0:
                check_neightbors(self.xpos-1, self.ypos-1)
            if self.ypos != VSIZE:
                check_neightbors(self.xpos-1, self.ypos+1)

        if self.xpos != HSIZE-1:
            check_neighbors(self.xpo+1, self.ypos)
            if self.ypos != 0:
                check_neightbors(self.xpos+1, self.ypos-1)
            if self.ypos != VSIZE:
                check_neightbors(self.xpos+1, self.ypos+1)

        if self.ypos != 0:
            check_neighbors(self.xpos, self.ypos-1)

        if self.ypos != VSIZE-1:
            check_neighbors(self.xpos, self.ypos+1)


    def be_born(self, neighbors):
        if self.status == 0:
            if neighbors in self.numtobirth:
                self.status = 1


    def die(self, neighbors):
        if self.status == 1: 
            if neighbors not in self.numtolive:
                self.status = 0

