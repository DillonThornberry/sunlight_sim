import numpy as np

class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

FRONT_RAIL = Rectangle(np.array([0, 0, 108]), np.array([0, 525, 0]))
BACK_WALL = Rectangle(np.array([192, 0, 244]), np.array([192, 327, 0]))
DOOR = Rectangle(np.array([192, 327, 0]), np.array([92, 525, 244]))
NORTH_WALL = Rectangle(np.array([0, 525, 244]), np.array([92, 525, 0]))
SOUTH_WALL = Rectangle(np.array([0, 0, 0]), np.array([192, 0, 244]))
SOUTH_PILLAR = Rectangle(np.array([0, 0, 50]), np.array([0, 300, 0]))
CEILING = Rectangle(np.array([0, 0, 244]), np.array([192, 525, 244]))

OBSTRUCTIONS = [FRONT_RAIL, BACK_WALL, DOOR, NORTH_WALL, SOUTH_WALL, SOUTH_PILLAR, CEILING]
