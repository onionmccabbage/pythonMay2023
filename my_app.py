# we can import other modules for use within this module
# import my_utility
# we can choose to import just parts of anotehr module
from my_utility import check
# Careful - any sort of import will ALWAYS run 
# the immediate code of that module

# Whatever module is being run will be
# given the __name__ '__main__' by Python

# it is a really good idea to ALWAYS check for __main__
if __name__ == '__main__':
    print(f'This module goes by the name {__name__}')