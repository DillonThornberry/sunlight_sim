from suncalc import get_position, get_times
from datetime import datetime, timedelta
from math import pi, degrees, sin, cos
import numpy as np
import pygame as pg
from obj import Rectangle, OBSTRUCTIONS

my_location = (39.734644019874075, -104.99554724682059)
# (39.7, -105)
time = datetime.now() - timedelta(hours=0)
arr = np.array

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

SW_CORNER = arr([OBSTRUCTIONS[0].topleft[0],OBSTRUCTIONS[0].topleft[1]])
SE_CORNER = arr([OBSTRUCTIONS[0].bottomright[0], OBSTRUCTIONS[0].bottomright[1]])
NW_CORNER = arr([OBSTRUCTIONS[0].bottomright[0], OBSTRUCTIONS[0].bottomright[1]])
MN_CORNER = arr([92, 350])
ME_CORNER = arr([192, 250])

def s(vec2):
    rot = arr([[0, 1], [-1, 0]])
    flip = arr([[1,0], [0,-1]])
    scale = (.75 * SCREEN_WIDTH) / (NW_CORNER[1] - SW_CORNER[1])
    shift = arr([.12 * SCREEN_WIDTH, .25 * SCREEN_HEIGHT])
    output = vec2.copy()
    output = np.dot(rot, vec2)
    output = np.dot(flip, output)
    output = output.astype(float) + shift
    output = output.astype(float) * scale
    return output





def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.draw.line(screen, (255,255,255), s(SW_CORNER), s(NW_CORNER))
    pg.draw.line(screen, (255,255,255), s(NW_CORNER), s(MN_CORNER))
    pg.draw.line(screen, (255,255,255), s(MN_CORNER), s(ME_CORNER))
    pg.draw.line(screen, (255,255,255), s(ME_CORNER), s(SE_CORNER))
    pg.draw.line(screen, (255,255,255), s(SE_CORNER), s(SW_CORNER))
    pg.display.flip()

    lat = input("Enter lat: ")
    lon = input("Enter lon: ")

    pg.quit()

    try:
        lat = float(lat)
    except ValueError:
        lat = my_location[0]

    try:
        lon = float(lon)
    except ValueError:
        lon = my_location[1] 
        
    pos = get_position(time, my_location[1], my_location[0])
    deg = pos.copy()
    for key in deg:
        None
        deg[key] = degrees(deg[key])

    print(pos)
    print(deg)
    vec = posVector(pos)
    print('(', vec[0], ',', vec[1], ',', vec[2], ')')
    print(np.linalg.norm(posVector(pos)))
    return

def posVector(pos):
    azi = pos['azimuth']
    alt = pos['altitude']
    return np.array([-sin(azi), -cos(azi), sin(alt)])

if __name__ == "__main__":
    main()