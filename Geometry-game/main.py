from math import sqrt
from random import randint

def distance(x,y):

    dist = sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
    return dist

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lowleft, upright):
        point = (self.x, self.y)
        if (self.x > upright[0] or self.x < lowleft[0]) \
        or (self.y > upright[1] or self.y < lowleft[1]):
            return print(f"The point {point}does not fall in the rectangle)")
        else:
            origin = (float(lowleft[0]+upright[0])/2,float(lowleft[1]+upright[1])/2)
            distance_from_origin = distance(origin, point)
            dist = format(distance_from_origin, ".2f")
            return print(f"The point {point} falls in the rectangle \n\
The Distance from origin {origin} is {dist}")

code = 0
while(code == 0):
    bottomleft = (randint(0,9),randint(0,9))
    topright = (randint(bottomleft[0],10),randint(bottomleft[1],10))
    print(f"Geometry game\n\nThe given coordinates {bottomleft}, {topright} are the bottom left and top right coordinates of a rectangle\n\n\
Enter the coordinates of a point that's inside the given rectangle\n")
    x = float(input("Enter the X coordinate of a point"))
    y = float(input("Enter the Y coordinate of a point"))

    point1 = Point(x,y)
    Answer = point1.falls_in_rectangle(bottomleft,topright)

    control = input('''If you want to continue the game Enter 1 or "continue".\nIf you want to end the game Enter 0 or "end".''')
    if control == 0 or "end":
        code == 1
