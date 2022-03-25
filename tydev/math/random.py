import random
import colorsys

def integer(min, max):
    return random.randint(int(min), int(max))

def float(min, max):

    r = random.random()
    return ((max - min) * r) + min

def color():

    return (integer(0, 255), integer(0, 255), integer(0, 255))

def shade(color):
    c = color
    colorsys.rgb_to_hsv(c[0]/255, c[1]/255, c[2]/255)

def vector(multiplier=0.0):

    x = float(0, 1) * multiplier
    y = float(0, 1) * multiplier

    if integer(0, 1) == 1:
        x *= -1
    if integer(0, 1) == 1:
        y *= -1

    return (x, y)

def location(x, y, xmax, ymax):

    _x = integer(x, xmax)
    _y = integer(y, ymax)

    return (_x, _y)