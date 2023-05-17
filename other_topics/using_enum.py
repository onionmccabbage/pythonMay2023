# we can enumerate values with enum
# This can be useful for working with constants

# simple constants exist in a tuple (by convention we CAPITALIZE the names of constants)
my_constants = ('MOUSE', 'KEYBOARD', 'STREAM', 'GPS')
event_type = my_constants[0]

# if we need more control we would use enum
from enum import Enum  # this is available in Python
class Colour(Enum): # this class extends the enum object
    RED   = 1
    GREEN = 2
    BLUE  = 3

n=1
print( Colour.RED.value) # access our 'constant'
if Colour.RED.value == n:
    print('The colour is red')