from enum import Enum

class Action(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    NO_OP = 5

class Board(Enum):
    EMPTY = "👣"
    WALL = "🟦"
    PLAYER = "🤖"


class Location:
    def __init__(self, x,y):
        self.x = x
        self.y = y
