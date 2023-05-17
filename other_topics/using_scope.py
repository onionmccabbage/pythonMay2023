# Anything that is not indented is in the global scope (or namespace)

# in all programming languages we try to avoid polluting the global scope
s = 'this is in the global scope'

def fn(): # all functions MUST have brackets (even if there are no arguments)
    # we can access global variables like this
    global s
    # this is a code block, it has its own scope
    # ... but we are refering to the global value s
    s = 'this is in the local scope of this code block'
    print(s)

if __name__ == '__main__':
    fn()
    print(s)

