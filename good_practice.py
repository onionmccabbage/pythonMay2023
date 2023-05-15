# Python generally uses functions for code blocks

# we define a function using 'def'
# ALL code blocks MUST use consistent indentation
# Generally we use one tab (four spaces)
def makeSquare(n): # arguments can be passed in via the brackets
    '''Return the square of the argument'''
    result = n**2 # or n*n
    return result # there is no obligation to return, but return will end the function

# NB in Python there is no 'overload'
def power(m, n):
    """Document your code using docstring
       The triple-quotes allows the use of new lines in your documentation"""
    return m**n # we can just return a value

# user input

# range and generators

# conditional logic, validation and type casting



# double-equals will CHECK equality (single equals will SET equality)
if __name__ == '__main__': # this is good practice
    print( makeSquare(3) ) # 3 squared is 9
    print( makeSquare(5) ) # 5 squared is 25
    print( power(2, 3) )   # 8
    print( power(4, 2) )   # 16
    print( power(9, 4) )   # 6561