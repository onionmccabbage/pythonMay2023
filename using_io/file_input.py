# we can read text back from a file

def readText():
    '''open a file then read the content'''
    # NB it would be a good idea to try-except this code
    # using the 'with' operator will close the file when done

    # Question if there is an excpetion, does 'with' still close the file???
    try:
        with open('my_file.txt', 'rt') as fin: # 'rt' will read text
            # r = fin.read() # here we read the entire file as one text string
            # r = fin.readline() # this will read just one line as a text string
            r = fin.readlines() # all the content is returns into a LIST of text strings
            # try to write to the file!!! 
        return r
    except FileNotFoundError as err:
        print(f'File does not exist {err}')
    finally:
        # even if there is an exception, the with operator STILL closed the input file
        isItClosed = fin.read() # nope iot has been closed
if __name__ == '__main__':
    print( readText() )