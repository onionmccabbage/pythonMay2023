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

# user input. CAREFUL every user input will be a string
def userInput():
    num = input('please enter a number: ')
    num_i = int( float(num) ) # good idea to FIRST cast as a float, THEN as an int
    # maybe we need to validate the number
    # conditional logic, validation and type casting
    if num_i >0 and num_i < 10: # >= <= !=
        print(num_i, type(num_i))
    elif num_i == 0: # optional elif clause (might be several 'elif')
        print('sorry we cannot handle zero at this time')
    else:
        print('number needs to be between 0 and 10')

# range and generators
def checkNumber(x):
    r = range(0, 15) # start, stop-before, step
    return x in r # does the number exist in the range?


# double-equals will CHECK equality (single equals will SET equality)
if __name__ == '__main__': # this is good practice
    print( makeSquare(3) ) # 3 squared is 9
    print( makeSquare(5) ) # 5 squared is 25
    print( power(2, 3) )   # 8
    print( power(4, 2) )   # 16
    print( power(9, 4) )   # 6561
    userInput() # note it takes no arguments
    print( checkNumber(3) ) # check if 3 is in the range(0-15) (0 to 14)