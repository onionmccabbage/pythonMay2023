# This class will encapsulate a 'user'
# The name will be a non-empty string
# the email will also be a non-empty string

# As a rule anything 'dunder' belongs to Python
# 'dunder' means double-underscore
# __name__, __str__ etc,

class User(): # we implicitly inherit from 'object'
    # we can have properties that belong to the class (NOT to any instance)
    userCount = 0 # this is like a static property
    # we can limit the arbitrary properties
    __slots__ = ['__n', '__e'] # only permit these properties
    def __init__(self, n, e):
        # we can prevent direct access to the properties
        self.n = n 
        self.e = e # self.e will call the property setter setEmail()
        User.userCount += 1 # increment the static property
    def __str__(self):
        return f'User {self.__n} has an email {self.__e}'
    def setName(self, new_name): #the setter or mutator method
        if type(new_name)==str and new_name != '':
            # using __ is called 'mangling'
            self.__n = new_name # __ will prevent direct access (similar to 'private' in Java)
        else:
            self.__n = 'Default' # or we could raise an exception
    def getName(self): # the getter or accessor method
        return self.__n
    def setEmail(self, new_email):
        if type(new_email)==str and new_email != '':
            self.__e = new_email
        else:
            self.__e = None
    def getEmail(self):
        return self.__e
    # we can make our getter/setter methods appear like normal properties (i.e. no brackets)
    n = property(getName, setName)
    e = property(getEmail, setEmail) # this makes sure we can validate the email
    
if __name__ == '__main__':
    l = User('Leanne', 'l@e.ie')
    # we can try to alter the name
    l.setName('Leonie')
    # NB the next line tries to add an arbitrary property to our instance
    # l.__n = 'Lovely' # will not change the name of the instance
    print(l)
    print( l.getName() ) # we can no longer directly access the __ values
    # we can use n to access setName and getName
    l.n = 'Lorraine' # this accesses the setName method as if it was a proeprty called n
    print(l.n) # this accesses the getName method as if it was the property n