class Cell(object):

    def __init__(self, pos):
        self.neighbors = 0
        self.neighbor_list = []
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]


    def add_neighbors(self):
        self.neighbor_list = []

        for i in xrange(self.x-1, self.x+1):
            for j in xrange(self.y-1, self.y+1):
                self.neighbor_list.append((i,j))

        self.neighbor_list.remove(self.pos)

        return self.neighbor_list


class Pattern(object):

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]

        patterns = {}

        patterns['block': [[1,1],
                           [1,1]]]

        patterns['beehive': [[0,1,1,0],
                             [1,0,0,1],
                             [0,1,1,0]]]

        patterns['loaf': [[0,1,1,0],
                          [1,0,0,1],
                          [0,1,0,1],
                          [0,0,1,0]]]

        paterns['boat': [[1,1,0],
                         [1,0,1],
                         [0,1,0]]]

        patterns['blinker': [[1,1,1]]]

        patterns['toad': [[0,1,1,1],
                          [1,1,1,0]]]

        patterns['beacon': [[1,1,0,0],
                            [1,1,0,0],
                            [0,0,1,1],
                            [0,0,1,1]]]

        patterns['pulsar': [[0,0,1,1,1,0,0,0,1,1,1,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [1,0,0,0,0,1,0,1,0,0,0,0,1],
                            [1,0,0,0,0,1,0,1,0,0,0,0,1],
                            [1,0,0,0,0,1,0,1,0,0,0,0,1],
                            [0,0,1,1,1,0,0,0,1,1,1,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,1,1,1,0,0,0,1,1,1,0,0],
                            [1,0,0,0,0,1,0,1,0,0,0,0,1],
                            [1,0,0,0,0,1,0,1,0,0,0,0,1],
                            [1,0,0,0,0,1,0,1,0,0,0,0,1],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,1,1,1,0,0,0,1,1,1,0,0]]

        patterns['glider': [[0,1,0],
                            [0,0,1],
                            [1,1,1]]]

        patterns['lwss': [[1,0,0,1,0],
                          [0,0,0,0,1],
                          [1,0,0,0,1],
                          [0,1,1,1,1]]]


    def create_pattern(self):
        pattern = self.patterns[self.name]
        coordinates = []

        for y in len(pattern):
            for x in len(pattern[y]):
                if pattern[x][y] == 1:
                    corrdinates.append((self.x+x, self.y+y))

        return coordinates
