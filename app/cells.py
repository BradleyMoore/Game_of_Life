class Cell(object):

    def __init__(self, xpos, ypos, numtobirth, numtolive):
        self.neighbors = []
        self.num_of_neighbors = 0
        self.numtobirth = numtobirth
        self.numtolive = numtolive
        self.status = 0
        self.xpos = xpos
        self.ypos = ypos
        self.pos = (xpos, ypos)


    def find_neighbors(self, hsize, vsize):

        self.sum_of_neighbors = 0
        possible_neighbors = []
        self.neighbors = []
        
        tl = (self.xpos-1, self.ypos-1)
        t = (self.xpos, self.ypos-1)
        tr = (self.xpos+1, self.ypos-1)
        l = (self.xpos-1, self.ypos)
        r = (self.xpos+1, self.ypos)
        bl = (self.xpos-1, self.ypos+1)
        b = (self.xpos, self.ypos+1)
        br = (self.xpos+1, self.ypos+1)

        if self.xpos != 0:
            self.possible_neighbors.append(l)
            if self.ypos != 0:
                self.possible_neighbors.append(tl)
            elif self.ypos != vsize:
                self.possible_neighbors.append(bl)
        elif self.xpos != hsize:
            self.possible_neighbors.append(r)
            if self.ypos != 0:
                self.possible_neighbors.append(tr)
            elif self.ypos != vsize:
                self.possible_neighbors.append(br)

        if self.ypos != 0:
            self.possible_neighbors.append(t)
            if self.xpos != 0:
                self.possible_neighbors.append(tl)
            elif self.xpos != hsize:
                self.possible_neighbors.append(tr)
        elif self.ypos != vsize:
            self.possible_neighbors.append(b)
            if self.xpos != 0:
                self.possible_neighbors.append(bl)
            elif self.xpos != hsize:
                self.possible_neighbors.append(br)

        self.neighbors = list(set(possible_neighbors))

        for location in self.neighbors:
            self.num_of_neighbors = self.num_of_neighbors + 1

        return self.neighbors


    def birth(self):
        if self.status == 0:
            if self.num_of_neighbors in self.numtobirth:
                self.status = 1


    def death(self):
            if self.num_of_neighbors not in self.numtolive:
                self.status = 0


    def reap_and_sow(self):
        if self.status == 1: 
            self.death()
        else:
            self.birth()

