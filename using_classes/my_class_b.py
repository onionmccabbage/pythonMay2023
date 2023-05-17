# Here we  will define a class to encapsulate a point in 2-d space
# There will be a floating point value for x and for y
# We will derive the hypotenuse from x and y: h = (x*x+y*y)**0.5

# the brackets are optional
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def hypotenuse(self):
        h = (self.x**2 + self.y**2)**0.5
        return h
    # we can override the built-in methods of object
    def __str__(self):
        return f'The point at x:{self.x} y:{self.y} has a hypotenuse of {self.hypotenuse()}'
    
if __name__ == '__main__':
    pointA = Point(3, 4)
    pointB = Point(8, 2)
    # NB every call to 'print' will use the built-in __str__ method
    print( pointA )
    print( pointA.hypotenuse() ) # 5.0
    print( pointB.hypotenuse() )