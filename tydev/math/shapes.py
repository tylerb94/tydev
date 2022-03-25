import math



class Rect:

    def __init__(self, width, height, location):
        self.width = width
        self.height = height
        self.location = location

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2

    def is_tall(self):
        return self.height > self.width

    def is_wide(self):
        return self.width > self.height

    def is_square(self):
        return self.width > self.height

    def get_size(self):
        s = (self.width, self.height)
        return s

    def get_rect(self):
        r = (self.location[0], self.location[1], self.width, self.height)
        return r

class Circle:

    def __init__(self, location, ):

        self.location = location
        self.radius = radius

    def circumfrence(self):
        return 2 * self.radius * tydev.math.pi

    def area(self):
        return tydev.math.pi * self.radius ** 2

    def radius(self):
        return self.radius

    def diameter(self):
        return 2 * self.radius

class Triangle:

    def __init__(self, points, location=(0.0, 0.0)):

        self.points = points
        self.location = location

    def area(self):

        x1 = points[0][0]
        y1 = points[0][1]
        x2 = points[1][0]
        y2 = points[1][1]
        x3 = points[2][0]
        y3 = points[2][1]

        area = x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 - y3*x1
        area /= 2
        area = abs(area)

        return area

    def perimiter(self):

        x1 = points[0][0]
        y1 = points[0][1]
        x2 = points[1][0]
        y2 = points[1][1]
        x3 = points[2][0]
        y3 = points[2][1]

        perimiter = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        perimiter += math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
        perimiter += math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

        return perimiter

