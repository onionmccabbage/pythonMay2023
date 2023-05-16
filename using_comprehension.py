# comprehension means to comprehensively deal with every member of a collection
# as we saw before, a list or a generator can iterate 
# over all the members of a range comprehensively

def comp(start=0, stop=10):
    '''This function will comprehensively deal with every member from start to stop'''
    r = range(start, stop) # use our arguments to make a range
    # here we make a collection of wavelengths by doubling numbers
    l = [ num*2 for num in r  ] # a list (in memory)
    g = ( num*2 for num in r )  # a generator (values are not stored in memory)

def dictComp():
    '''we can comprehensively deal with every member of a dictionary
       this is known as dictionary comprehension in Python'''
    p = 'are we there yet' # this is a simple immutable string of characters
    chars_d = { letter:p.count(letter) for letter in p }
    print( chars_d )


if __name__ == '__main__':
    comp(-99, 100)
    dictComp()
