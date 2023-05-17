# Remember, generators are efficient because their values never persist in memory

def genSquareNums(n=1, stop=10):
    '''Yield each square number in turn'''
    number = n
    while number < stop:
        # the 'yield' statement makes this function into a generator
        yield number**2 #  yield the square of each value (not return)
        number += 1

if __name__ == '__main__':
    # make use of the custom generator
    my_g = genSquareNums() # use the default values
    print( type(my_g) )
    print( my_g.__next__() ) # 1
    print( my_g.__next__() ) # 4
    # since it is a generator we can iterate over it
    for i in my_g:
        print(f'The next square nubmer is {i}')