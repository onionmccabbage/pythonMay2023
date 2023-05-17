# This class will encapsulate a 'user'
# The name will be a non-empty string
# the email will also be a non-empty string

class User(): #we implicitly inherit from 'object'
    def __init__(self, n, e):
        # we can prevent direct access to he properties
        # using __ is called 'mangling'
        self.__n = n # __ will prevent direct access (similar to 'private' in Java)
        self.__e = e
    def __str__(self):
        return f'User {self.__n} has an email {self.__e}'
    def setName(self, new_name): #the setter or mutator method
        if type(new_name)==str and new_name != '':
            self.__n = new_name
        else:
            self.__n = 'Default' # or we could raise an exception
    def getName(self): # the getter or accessor method
        return self.__n
    
if __name__ == '__main__':
    l = User('Leanne', 'l@e.ie')
    # we can try to alter the name
    l.setName('Leonie')
    # NB the next line adds an arbitrary proerty to our instance
    l.__n = 'Lovely' # will not change the name of the instance
    print(l)
    print( l.getName() ) # we can no longer directly access the __ values