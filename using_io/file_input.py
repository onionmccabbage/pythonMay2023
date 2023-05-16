# we can read text back from a file

def readText():
    '''open a file then read the content'''
    # using the 'with' operator will close the file when done
    with open('my_file.txt', 'rt') as fin: # 'rt' will read text
        # r = fin.read() # here we read the entire file as one text string
        # r = fin.readline() # this will read just one line as a text string
        r = fin.readlines() # all the content is returns into a LIST of text strings
    return r

if __name__ == '__main__':
    print( readText() )