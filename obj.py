import numpy as np

class Rectangle:
    def __init__(self, name, topleft, bottomright, topright, bottomleft):
        self.name = name
        self.topleft = topleft
        self.bottomright = bottomright
        self.topright = topright
        self.bottomleft = bottomleft

FRONT_RAIL = Rectangle("front rail", np.array([0, 0, 108]), np.array([0, 525, 0]), np.array([0, 525, 108]), np.array([0, 0, 0]))
BACK_WALL = Rectangle("east wall", np.array([192, 0, 244]), np.array([192, 327, 0]), np.array([192, 327, 244]), np.array([192, 0, 244]))
DOOR = Rectangle("door", np.array([92, 525, 244]), np.array([192, 327, 0]), np.array([192, 327, 244]), np.array([92, 525, 0]))
NORTH_WALL = Rectangle("north wall", np.array([0, 525, 244]), np.array([92, 525, 0]), np.array([92, 525, 244]), np.array([0, 525, 0]))
SOUTH_WALL = Rectangle("south wall", np.array([192, 0, 244]), np.array([0, 0, 0]), np.array([0, 0, 244]), np.array([192, 0, 0]))
SOUTH_PILLAR = Rectangle("south pillar", np.array([192, -900, 1000]), np.array([0, -900, 0]), np.array([0, -900, 1000]), np.array([192, -900, 0]))
CEILING = Rectangle("ceiling", np.array([0, 0, 244]), np.array([192, 525, 244]), np.array([0, 525, 244]), np.array([192, 0, 244]))

OBSTRUCTIONS = [FRONT_RAIL, BACK_WALL, DOOR, NORTH_WALL, SOUTH_WALL, SOUTH_PILLAR, CEILING]
