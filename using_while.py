# we can use 'while' to make a run-loop
# CAREFUL - you need away to break out of the loop

def main():
    '''This function will run endlessly, or until we break out of the loop'''
    flag = True
    while flag:
        r = input('say hello: ')
        if r == 'hello':
            flag=False
            # break # this will break out of the loop
        else:
            continue # useful to just carry on

if __name__ == '__main__':
    main()
