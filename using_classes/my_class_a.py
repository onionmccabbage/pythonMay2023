# Classes can be useful to encapsulate important features in a data structure

class Person:
    '''This class encapsulates a persons name (string) and age (int) '''
    # 'self' represents the current instance of the class (like 'this' in Java)
    def __init__(self, n, a): # this is like a constructor in Java
        '''__init__ is the initializer method for this function
           Every time a new instance is created, this function will run'''
        self.n = n # we asign the incoming arguments to properties of an instance
        self.a = a
    # we can also define functions that belong to the class
    # These are known as methods (but they are just functions)
    def showInfo(self): # any method of a class MUST take 'self' as an argment
        return f'I am {self.n} and my age is {self.a}'
    def birthday(self):
        self.a += 1
    
# class properties are things the class has
# class methods are things the clas can do

# Remember - Python already has data structures like List, Tuple, String etc.

if __name__ == '__main__':
    '''we can make instances of our class'''
    p1 = Person('Timnit', 42)
    p2 = Person('Ethel', 32)
    # we can mutate the instance properties
    p1.a = 43
    p1.birthday()
    # now we can see the instances and their values
    print( p1.showInfo() )





    # we can make new instances of any structure
    t1 = tuple() # shortcut ()
    l1 = list()  # shortcut []
    l2 = list()
    i1 = int()
    f1 = float()
    d1 = dict()
    s1 = str()   # shortcut ''  or ""