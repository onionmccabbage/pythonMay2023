# we can override ANY built-in feature of Python
# e.g. __str__() will override how we print a class
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other

class BrokenMaths():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        '''instead of normal addition, we will make a string'''
        result = f'{str(self.x)}+{other.y}'
        return result

if __name__ == '__main__':
    p = BrokenMaths(1, 2)
    r = BrokenMaths(3, p.y)
    s = BrokenMaths(7, r.y)
    # here the plus-sign '+' will call __add__
    print(r+s) # 
