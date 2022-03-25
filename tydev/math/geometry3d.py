import math


def angle_from_2_points_d(origin_point, second_point):

    p = (second_point[0] - origin_point[0], second_point[1] - origin_point[1])
    o = (0, 0)
    a = 0.0

    if not p[0] == 0:
        s = p[1] / p[0]
        a = math.atan(s)

    return a

def point_dist(point_a, point_b):

    x = abs(point_a[0] - point_b[0]) ** 2
    y = abs(point_a[1] - point_b[1]) ** 2
    z = abs(point_a[2] - point_b[2]) ** 2

    d = math.sqrt(x + y + z)
    return d