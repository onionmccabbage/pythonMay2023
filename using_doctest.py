# it is a VERY good idea to test your code
#  'unit testng' means testing individual units of code
# If we write modules and functions, it is easy to test bits of code
import doctest

def cube(x):
    '''return the cube of x. Doctetst is written like this:
    >>> cube(3)
    27
    >>> cube(100)
    1000000
    >>> cube(-3)
    -27
    '''
    return x**3

def findSquareRoot(y):
    '''return the square root of a value
    >>> findSquareRoot(9)
    3.0
    >>> findSquareRoot(25)
    5.0
    '''
    return y**0.5 # anything raised to the power of 0.5 will be the square root


if __name__ == '__main__':
    '''run unit tests'''
    # print( cube(3) ) # 27
    doctest.testmod(verbose=True) # here we start our document tests