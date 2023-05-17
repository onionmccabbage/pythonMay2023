# This class will encapsulate a 'user'
# The name will be a non-empty string
# the email will also be a non-empty string

class User(): #we implicitly inherit from 'object'
    def __init__(self, n, e):
        self.n = n
        self.e = e
    def __str__(self):
        return f'User {self.n} has an email {self.e}'
    
if __name__ == '__main__':
    l = User('Leanne', 'l@e.ie')
    print(l)