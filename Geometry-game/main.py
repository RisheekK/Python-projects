from math import sqrt

def distance(x,y):

    dist = sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
    return dist

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lowleft, upright):
        if (self.x > upright[0] or self.x < lowleft[0]) \
        and (self.y > upright[1] or self.y < lowleft[1]):
            return False
        else:
            point = (self.x, self.y)
            origin = (float(lowleft[0]+upright[0])/2,float(lowleft[0]+upright[0])/2)
            distance_from_origin = distance(origin, point)
            print(f"The point ({point[0]},{point[1]}) falls in the rectangle \n\
                The Distance from origin {origin} is {distance_from_origin}")

