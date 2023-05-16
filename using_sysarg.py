# We can pass arguments in to our module when we run it
import sys

# by default a single system argument variable (sys.argv) is passed in
# Any other parameters will also be included in the sys.argv list
for i in sys.argv:
    # careful - ALL sys.argv are STRING values
    print( i, type(i) ) # each sys.argv is indexed in a list (indexed 0, 1, 2 etc.)