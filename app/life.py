class Cell(object):

    def __init__(self, pos):
        self.neighbors = 0
        self.neighbor_list = []
        self.pos = pos
        self.posx = pos[0]
        self.posy = pos[1]

    def add_neighbors(self):
        self.neighbor_list = []

        for x in xrange(self.posx-1, self.posx+1):
            for y in xrange(self.posy-1, self.posy+1):
                self.neighbor_list.append((x,y))

        self.neighbor_list.remove(self.pos)

        return self.neighbor_list
