# Python has range and generator objects
# These are useful for efficient coding
def useRange():
    # a range lets us handle ranges of numeric values
    r = range(-99, 100, 2) # start, stop-before, step
    print( type(r) ) # a range object will generate the values when we need them
    # thje numeric values CAN exist in memory
    r_t = tuple(r) # remember this uses more memory - the values exist in memory
    print( r_t )
    # we can iterate over a range
    for _ in r:
        print(_, end=', ') # by default print will put a new line at the end. We can override

# remember: in Python a code block begins with a colon and ends when we stop indentation
def createLists():
    # we can use a range to populate generated structures. (i.e. the range becomes a generator)
    odd_list = [ num for num in range(-99, 100) if num%2 == 1 ]
    print(odd_list)
    # remember, the list will use memory, but the generator does not
    squares_list = [ num*num for num in range(1,101) ]
    print(squares_list)

def createTuple():
    # first we make a generator
    g = ( num/4 for num in range(-25, 26) )
    # then we make a tuple
    t = tuple(g)
    return t

def makeGen():
    # we can make a generator (instead of a list or tuple)
    even_generator = ( num for num in range(-100, 101) if num%2 == 0 ) # or step 2
    print( type(even_generator) ) # we have aa generator (the values do not use up memory)
    # we can access members from our generator
    print( even_generator.__next__() ) # this will yield the next member fro mthe generator
    print( even_generator.__next__() ) # -98
    print( even_generator.__next__() ) # -96

    for _ in even_generator: # the generator will remember the position it got to
        print( _, end=', ' )

    # print( even_generator.__next__() ) # NOPE - the generator has ben exhausted!!

if __name__ == '__main__':
    useRange()
    createLists()
    makeGen()
    # see our generated tuple in action
    result_t = createTuple()
    print( type(result_t), result_t )