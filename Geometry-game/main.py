from math import sqrt
from random import randint

def distance(x,y):

    dist = sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
    return dist

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        point = (self.x, self.y)
        if (rectangle.bottomleft.x < self.x < rectangle.topright.x) and \
        (rectangle.bottomleft.y < self.y < rectangle.topright.y):
            origin = (float(rectangle.bottomleft.x + rectangle.topright.x)/2, float(rectangle.bottomleft.y + rectangle.topright.y)/2)
            distance_from_origin = distance(origin, point)
            dist = format(distance_from_origin, ".2f")
            return print(f"The point {point} falls in the rectangle \n\
The Distance from origin {origin} is {dist}")
        else:
            return print(f"The point {point} does not fall in the rectangle)")
        
class Rectangle:

    def __init__(self, bottomleft, topright):
        self.bottomleft = bottomleft
        self.topright = topright

code =0

while(code == 0):
    bottomleft = Point(randint(0,5),randint(0,5))
    topright = Point(randint(bottomleft.x+1,10), randint(bottomleft.y+1,10))
    rectangle = Rectangle(bottomleft, topright)
    print(f"\nGeometry game\n\nThe given coordinates \
({bottomleft.x},{bottomleft.y}) ({topright.x},{topright.y}) are the bottom left and top right coordinates of a rectangle\n\n\
Enter the coordinates of a point that's inside the given rectangle\n")
    x = float(input("Enter the X coordinate of a point -> "))
    y = float(input("Enter the Y coordinate of a point -> "))

    point1 = Point(x,y)
    Answer = point1.falls_in_rectangle(rectangle)

    control = input('''If you want to continue the game Enter 1 or "continue".\nIf you want to end the game Enter 0 or "end" -> ''')
    
    if control == 0 or control == "end":
        code = 1