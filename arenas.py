from env_objects import *
from maps import *

class Arena:
    def __init__(self, map = arena1_map):
        id_2_board = {1: Board.WALL, 0: Board.EMPTY}
        self.map = [[id_2_board[c_i] for c_i in row_i] for row_i in map]


        self.agent = Location(1,1)

        self.MAX_HEIGHT = len(self.map)
        self.MAX_WIDTH = len(self.map)
    
    def get_element(self, x, y):
        if (x < 0) or (x >= self.MAX_WIDTH) or (y < 0) or (y >= self.MAX_HEIGHT):
            raise Exception("invalid coordinates in get_element")
        else:
            return self.map[y][x] 

    def is_valid_position(self, x, y):
        valid_blocks = {Board.EMPTY}
        return self.get_element(x,y) in valid_blocks

    def visualize(self):
        str_rep = ""
        for row_i in range(self.MAX_HEIGHT):
            for c_i in range(self.MAX_WIDTH):
                if (self.agent.x == c_i) and (self.agent.y == row_i):
                    str_rep += Board.PLAYER.value
                else:
                    str_rep += self.get_element(c_i, row_i).value
            str_rep += '\n'
        return str_rep
    


arena = Arena(arena1_map)
print(arena.visualize())