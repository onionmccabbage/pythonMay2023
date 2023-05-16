# we know functions can take arguments, 
# and we can provide default values for those arguments

# python lets us handle positonal arguments and also keyword arguments

def usePostional(*args): # the asterisk tells python to gather all the positional arguments
    '''The arguments passed in to a function are called positional arguments
       They will all exist in a tuple (members 0, 1, 2 etc.)'''
    print( type(args), args )

def useKeyword(**kwargs): # the double-asterisk tells python to gather all the keyword arguemnts into a dictionary
    '''All keyword arguments passed in to a function will exist in a dictionary'''
    print( type(kwargs), kwargs )

# NB there is nothing special about the words 'args' or 'kwargs', they are conventional
def useBoth(*args, **kwargs): # the positional arguments MUST come before any keyword arguments
    '''Any positonal arguments end up in a tuple
       Any keyments end up in a dictionary'''
    print( f'The keword arguments are {args}' )
    for (k, v) in kwargs.items(): # all dictionaries will have an items() method
        print(f'they keyword {k} has the value {v}')



if __name__ == '__main__':
    # we pass positional arguments
    usePostional(3, 2, 1, 'string', False, None, {})
    useKeyword( c=5, z='spacial', b=False, t=(5,4,3,2) )
    useBoth('coffee', True, 876, [], useKeyword, 'done', fn=usePostional, prop='anything', d={'drink':'tea'} )
