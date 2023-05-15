# Python lets us name anything.
# In all cases there are some rules
# and also some conventions

# rules
# DO NOT use keywords for your identifier
# def = '3' # no can do!!!
# avoid identifiers that begin with a digit
# 1 = 9 # oops!!!
# identifiers cannot include a dash
# my-name= 'Broken' # no - it looks like mathematics

# conventions
# we tend to use lower case or camel case for function names and variable names
def thisIsCamelCase():
    pass
    this_is_snake_case = 'clever'
# Some people trail a type indicator
words_s = 'this is a string'
words_t = ('this', 'is', 'a', 'tuple')
words_l = ['items']
# by convention classes tend to have Initial Caps for their name
# this is called PascalCase
class MyClass: # this is the least code we can write for a class
    '''Class names do NOT need to be Caps - Python does not care'''

# Python does not implement contants. Use an immutable tuple value

# Using Quotes
s1 = 'Single quotes are fine'
s2 = "Double quotes are also fine"
s3 = '''Triple quotes let us write new line characters
The new line is preserved'''
s4 = """We can also use triple double quotes (still preserves whitespace)"""