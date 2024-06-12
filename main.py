from suncalc import get_position, get_times
from datetime import datetime, timedelta
from math import pi, degrees, sin, cos, tan
import numpy as np
import pygame as pg
from obj import OBSTRUCTIONS

my_location = (39.7, -105)
time = datetime.now() - timedelta(hours=12)
arr = np.array

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
RES_REDUCE = 1

SW_CORNER = arr([OBSTRUCTIONS[4].bottomright[0],OBSTRUCTIONS[4].bottomright[1]])
SE_CORNER = arr([OBSTRUCTIONS[4].topleft[0], OBSTRUCTIONS[4].topleft[1]])
NW_CORNER = arr([OBSTRUCTIONS[3].topleft[0], OBSTRUCTIONS[3].topleft[1]])
MN_CORNER = arr([OBSTRUCTIONS[3].bottomright[0], OBSTRUCTIONS[3].bottomright[1]])
ME_CORNER = arr([OBSTRUCTIONS[1].bottomright[0], OBSTRUCTIONS[1].bottomright[1]])


# Transform world coordinates to screen
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

# Get start positions for rays
def getGroundPositions():
    positions = []
    minTan = 2
    for x in range(1, SE_CORNER[0] - 1, RES_REDUCE):
        for y in range(1, NW_CORNER[1] - 1, RES_REDUCE):
            # Ignore points in bottom right corner
            if x > 92 and y > 327 and (((522 - y) / (x - 92)) < minTan):
                continue 
            positions.append(arr([x, y, 0]))
    
    return positions

def isInLight(startPos, sunAngle):
    for rect in OBSTRUCTIONS:
        side1 = rect.topright - rect.topleft
        side2 = rect.topleft - rect.bottomleft

        norm = np.cross(side1, side2)
        denom = np.dot(sunAngle, norm)

        # Ray and obstruction are parallel
        if np.abs(denom) < 1e-6:
            continue
        
        t = np.dot(norm, (rect.topleft - startPos) / denom)

        if t <= 0:
            continue

        hitPoint = startPos + t * sunAngle

        ap = hitPoint - rect.topleft

        sideDot1 = np.dot(side1, side1)
        sideDot2 = np.dot(side2, side2)

        hitDot1 = np.dot(side1, hitPoint)
        hitDot2 = np.dot(side2, hitPoint)

        if (0 <= hitDot1 <= sideDot1 and 0 <= hitDot2 <= sideDot2):
            return False

    return True


def main():

    positions = getGroundPositions()
    print(len(positions))

    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.draw.line(screen, (255,255,255), s(SW_CORNER), s(NW_CORNER))
    pg.draw.line(screen, (255,255,255), s(NW_CORNER), s(MN_CORNER))
    pg.draw.line(screen, (255,255,255), s(MN_CORNER), s(ME_CORNER))
    pg.draw.line(screen, (255,255,255), s(ME_CORNER), s(SE_CORNER))
    pg.draw.line(screen, (255,255,255), s(SE_CORNER), s(SW_CORNER))
    pg.display.flip()

    sunPos = get_position(time, my_location[1], my_location[0])
    sunVec = posVector(sunPos)
    sunVec = sunVec / np.linalg.norm(sunVec)
    
    for p in positions:
        if not isInLight(p, sunVec):
            continue
        p = arr([p[0], p[1]])
        p = s(p)
        p = [int(p[0]), int(p[1])]
        screen.set_at(p, (200, 0, 0))
    print(sunVec)
    pg.display.flip()
    
    input("Complete")

    pg.quit()

    '''
    lat = input("Enter lat: ")
    lon = input("Enter lon: ")

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
    '''
    return

def posVector(pos):
    azi = pos['azimuth']
    alt = pos['altitude']
    return np.array([-sin(azi), -cos(azi), sin(alt)])

if __name__ == "__main__":
    main()