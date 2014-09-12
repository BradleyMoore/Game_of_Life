class Cell(object):

    def __init__(self, xpos, ypos, numtobirth, numtolive):
        self.possible_neighbors = []
        self.neighbors = 0
        self.numtobirth = numtobirth
        self.numtolive = numtolive
        self.status = 0
        self.xpos = xpos
        self.ypos = ypos
        self.pos = (xpos, ypos)


    def check_neighbor(self, neighbor):
        if neighbor.satus == 1:
            self.neighbors = self.neighbors + 1


    def find_neighbors(self, hsize, vsize):
        self.possible_neighbors = []
        self.neighbors = 0
        if self.xpos != 0:
            self.possible_neighbors.append((self.xpos-1, self.ypos))
            if self.ypos != 0:
                self.possible_neighbors.append((self.xpos-1, self.ypos-1))
            if self.ypos != vsize:
                self.possible_neighbors.append((self.xpos-1, self.ypos+1))

        if self.xpos != hsize-1:
            self.possible_neighbors.append((self.xpos+1, self.ypos))
            if self.ypos != 0:
                self.possible_neighbors.append((self.xpos+1, self.ypos-1))
            if self.ypos != vsize:
                self.possible_neighbors.append((self.xpos+1, self.ypos+1))

        if self.ypos != 0:
            self.possible_neighbors.append((self.xpos, self.ypos-1))

        if self.ypos != vsize-1:
            self.possible_neighbors.append((self.xpos, self.ypos+1))

        return self.possible_neighbors


    def check_for_birth(self):
        if self.status == 0:
            if self.neighbors in self.numtobirth:
                self.status = 1


    def check_for_death(self):
            if self.neighbors not in self.numtolive:
                self.status = 0


    def reap_and_sew(self):
        if self.status == 1: 
            check_for_death()
        else:
            check_for_birth()

