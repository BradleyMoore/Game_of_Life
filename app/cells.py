class Cell(object):

    def __init__(self, xpos, ypos, numtobirth, numtolive):
        self.neighbors = []
        self.num_of_neighbors = 0
        self.status = 0
        self.numtobirth = numtobirth
        self.numtolive = numtolive
        self.xpos = xpos
        self.ypos = ypos
        self.pos = (xpos, ypos)


    def find_neighbors(self, hsize, vsize):

        self.sum_of_neighbors = 0
        possible_neighbors = []
        self.neighbors = []
        to_remove = []
        
        tl = (self.xpos-1, self.ypos-1)
        t = (self.xpos, self.ypos-1)
        tr = (self.xpos+1, self.ypos-1)
        l = (self.xpos-1, self.ypos)
        r = (self.xpos+1, self.ypos)
        bl = (self.xpos-1, self.ypos+1)
        b = (self.xpos, self.ypos+1)
        br = (self.xpos+1, self.ypos+1)

        possible_neighbors.append(tl)
        possible_neighbors.append(t)
        possible_neighbors.append(tr)
        possible_neighbors.append(l)
        possible_neighbors.append(r)
        possible_neighbors.append(bl)
        possible_neighbors.append(b)
        possible_neighbors.append(br)

        if self.xpos == 0:
            to_remove.append(tl)
            to_remove.append(l)
            to_remove.append(bl)
        elif self.xpos == hsize-1:
            to_remove.append(tr)
            to_remove.append(r)
            to_remove.append(br)

        if self.ypos == 0:
            to_remove.append(tl)
            to_remove.append(t)
            to_remove.append(tr)
        elif self.ypos == vsize-1:
            to_remove.append(bl)
            to_remove.append(b)
            to_remove.append(br)

        to_remove = list(set(to_remove))

        for item in to_remove:
            possible_neighbors.remove(item)

        self.neighbors = list(set(possible_neighbors))

        for location in self.neighbors:
            self.num_of_neighbors = self.num_of_neighbors + 1

        return self.neighbors


    def check_birth(self):

        for item in self.numtobirth:
            if self.num_of_neighbors == item:
                print 'born'
                self.status = 1
                break
        print '\n'


    def check_death(self):
        
        die = True
        for item in self.numtolive:
            if self.num_of_neighbors == item:
                die = False
        if die == True:
            self.status = 0


    def reap_and_sow(self):

        if self.status == 1:
            self.check_death()
        elif self.status == 0:
            self.check_birth()

