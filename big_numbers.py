# Python can handle very large numbers
import sys

def main():
    '''Here we will try to work with very large numbers'''
    print(10**100000) # Python has no limit on numbers other than system resources

def fnOp(a, op):
    '''There are a few useful shortcut operators in Python'''
    if op == '+':   
        a+=1 # increment a
    if op == '-':
        a-=1 # decrement a
    if op == '*':
        a *=a 
    if op == '/':
        a /=2 
    # there is no ++ or -- in Python
    return a


if __name__ == '__main__':
    main()
    print( fnOp(3, '+') ) # 4
    print( fnOp(3, '-') ) # 
    print( fnOp(3, '*') ) # 
    print( fnOp(3, '/') ) # 
    print( sys.maxsize ) # largest objectpermitted in memory
    print( sys.float_info) # the lagest and smallest floating point valurs Python will handle



