# Comments in Python are done like this
# basic numbers and maths
a = 3   # an integer (int)
b = 7.2 # float
c = 4
d = c/a # we are dividing an int by an int, the result is a float
e = a*b
f = b**a # raise to the power

# we can explore code with 'print'
print( type(a) ) # int
print( type(b) )
print( d, type(d) ) # float

# there are some unusual operators
g = b//a # integer division (but the result is a floating point number)
h = b%a  # modulo arithmetic
print( g, h )

# There are several collection data-types in Python
# e.g. string, tuple, list, set and dictionary
s = 'is it coffee yet?'
# we can access members of any ordinal collection using square brackets (zero-based)
print( s[7] )
# we can also get a slice of an ordinal collection like this
print( s[2:14:2] ) # start at position 2:stop-before position 7:step
# CAREFUL - strings are immutable (cannot be altered after creation)
# s[0] = 'I' # fail
s = 'Changed' # here we do not mutate s, we assign a new value to s
print( s[::-1] ) # here we step backwards through the index members
# some other string manipulation tools
string = 'coffee at eleven'
sentence = string.join('-') # we will revisit 'join'
print(sentence)
# list and tuple
# a tuple is an immutable indexed collection of any data types
t = (7, 5, 6, a, b, c, s) # round brackets indicate a tuple
print(t, type(t))
print( t[0:4:2] ) # [start:stop-before:step]
# a list is a mutable indexed collection of any data types
l = [b, c, True, a, g, (3,2,1), t, []] # square brackets indicate a list
l[0] = 'altered'
l.pop() # removes the last item
l.append('added item')
l.append(False)
print( l, type(l) )
# Always use a tuple, until you need a list!
# we can iterate over any ordered collection
for i in s:
    print(i) # print always puts a newline at the end
for i in l: # we could also iterate over the tuple
    print(i)

# Booleans etc: True and False and None

# The set collection. A mutable collection of unique values, not indexed by number
my_set = {1, a, 3, 't', 't', 3, 2, True} # 1 and True evaluate to the same thing
my_set.add(False)
# CAREFUL in a set we can EITHER have 1 OR True. We can EITHER have 0 OR False
print( my_set, type(my_set) )
# we can iterate over members of a set like this
for i in my_set:
    print(i)