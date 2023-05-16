# simple data types are passed by reference
# complex data types are passed by value

# by reference
e = 3
d = e # now e and d both reference the SAME value in memory
print(d, e)

# by value
b = {'key':'value'}
a = b
a['key']='changed'

print(a, b)

# what about immutable tuples - members are by REFERENCE
t = (a, b)
a['key']='mutated'
print(t)