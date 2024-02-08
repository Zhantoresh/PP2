"""
Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points

"""
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, jana_x, jana_y):
        self.x = jana_x
        self.y = jana_y

    def dist(self, ot):
        dis = math.sqrt((self.x - ot.x)**2 + (self.y - ot.y)**2)
        return dis

point1 = Point(1, 5)
point2 = Point(3, 8)

point1.show()
point2.show()

point1.move(5, 7)
point1.show()

distance = point1.dist(point2)
print(distance)