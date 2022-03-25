import math


def angle_to_vector_d(angle_d):

    a = math.radians(angle_d)
    x = math.cos(a)
    y = math.sin(a)
    return [x, y]

def surface_area_rect3d(length, width, height):

    area = 0.0

    if type(length) == any((int, float)):
        if length >= 0.0:

            if type(width) == any((int, float)):
                if width >= 0.0:

                    if type(height) == any((int, float)):
                        if height >= 0.0:

                            area += length * width * 2
                            area += length * height * 2
                            area += width * height * 2
    return area




def orbit(origin, point, angle):

    #Rotate a point counterclockwise by a given angle around a given origin.
    #The angle should be given in degrees.

    angle = math.radians(angle)
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return (qx, qy)
