from my_class_c import User

n = User('Alice', 42)

# All objects permit additonal properties in all cases
n.arb = 'this is an arbitrary property'
n.l = ['list', 'of', 'values']
n._______wow = 'this is entriely legal'
print(n, n.arb, n.l, n._______wow)
