# look at a few loose ends
import random # there are several libraries that come with Python

# using range and conditionals
def checkRandom(): # remember we must import random
    '''Generate a random integer number
       Then check if the random number is odd'''
    r = random.randint(0,10) # now we will get a random integer 0-10 inclusive
    # find out if r is an odd number
    # odd_b = r/2 != int(r/2)
    odd_b = r%2 != 0 # there are many ways to check for odd numbers
    # print(odd_b) # show True or False
    return (r, odd_b) # the function stops as soon as we call return

# function with default values
def checkIfEven(c=0): # here we give c the default value of 0. It can be overriden by a function call
    '''Return True or Fals based on c being even or odd'''
    return c%2 == 0 # True if even, Fals if odd

# dictionary collection: a mutable non-indexed collection of key-value pairs (of any data type)
def useDict():
    d = {'menu':'food', 'start':'12:30', 'end':'1:30', 'id':'lunchtime'}
    # dictionary is mutable
    d['offset'] = 2
    d['menu'] ='sustenance'
    return d

# good practice to use the following block
if __name__ == '__main__':
    answer = checkRandom()
    # we can format printed output: f'' creates a formatted string
    print(f'The number {answer[0]} is it odd: {answer[1]}') # see the random number
    # another way to write a formatted string
    print('The number {} is it odd: {}'.format(answer[0], answer[1]))
    # call a function, passing NO arguments (the default will be used)
    print( checkIfEven() )
    print( checkIfEven(99) ) # here we override the default with our own argument
    # use the dictionary functon
    d = useDict()
    print(f"for {d['id']} we start at {d['start']} and finish at {d['end']}")