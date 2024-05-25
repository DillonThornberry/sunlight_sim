import numpy as np

class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

FRONT_RAIL = Rectangle(np.array([0, 0, 50]), np.array([0, 300, 0]))
BACK_WALL = Rectangle(np.array([192, 0, 250]), np.array([0, 250, 0]))
DOOR = Rectangle(np.array([0, 0, 50]), np.array([0, 300, 0]))
NORTH_WALL = Rectangle(np.array([0, 0, 50]), np.array([0, 300, 0]))
SOUTH_WALL = Rectangle(np.array([0, 0, 50]), np.array([0, 300, 0]))
SOUTH_PILLAR = Rectangle(np.array([0, 0, 50]), np.array([0, 300, 0]))
CEILING = Rectangle(np.array([0, 0, 50]), np.array([0, 300, 0]))

OBSTRUCTIONS = [FRONT_RAIL, BACK_WALL, DOOR, NORTH_WALL, SOUTH_WALL, SOUTH_PILLAR, CEILING]
