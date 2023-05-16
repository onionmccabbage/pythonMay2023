# Python lets us write to files and read back from files
from datetime import datetime

def writeOutput(t):
    '''Here we take a text string t and write it out to a tezt file'''
    # NB if the file does not exist, use 'at' to append text
    # wt will (over)write existing text
    # xt will only work if the file does NOT exist 
    # (exclusive access)
    # by default we write text, so the 't' is optional
    fout = open('my_file.txt', 'at') # this is a file acess object
    print( t, file=fout ) # print lets us redirect output to a text file

if __name__ == '__main__':
    words = 'here is some text to be written to a file'
    d = datetime.today()
    writeOutput(str(d)) # make sure it is a string


