# here we can validate values

def check(value):
    '''check if the value is valid
       Here valid means a postive int
       greater than zero'''
    valid_flag = False
    if type(value)== int and value >0:
        valid_flag = True
    return valid_flag

if __name__ == '__main__':
    # exercise the code
    print( check(-1) ) # False
    print( check(1) )  # True
    print( check('oops') ) # False
    # if a module is imported, then that module 
    # will be given the __name__ of the module (my_utility in this case)
    print(f'This imported module goes by the name {__name__}')
