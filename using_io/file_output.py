# Python lets us write to files and read back from files
from datetime import datetime

def writeOutput(t):
    '''Here we take a text string t and write it out to a tezt file'''
    # NB if the file does not exist, use 'at' to append text
    # wt will (over)write existing text
    # xt will only work if the file does NOT exist 
    # (exclusive access)
    # by default we write text, so the 't' is optional ('b' for bytes)
    fout = open('my_file.txt', 'at') # this is a file acess object
    print( t, file=fout ) # print lets us redirect output to a text file
    fout.close() # good idea to always close our output file

def writeChunks(t):
    '''Here we write text in small chunks'''
    try:
        # fout = open('my_file.txt', 'x') # this will throw an exception (file exists)
        fout = open('my_file.txt', 'a') # NB default to text
        # now we will write small chunks ot text to the file
        size = len(t)
        offset = 0
        chunk  = 24 # here we choose to write 24 characters at a time
        while True:
            if offset>size:
                fout.write('\n') # we can write a new line character
                fout.close()
                break
            else:
                fout.write( t[offset:offset+chunk] ) # write a slice of our text to the file
                offset += chunk
    except FileExistsError as err:
        print(f'The file already exists {err}')
    except Exception as e:
        print(f'Something went wrong {e}')
    finally:
        '''finally will always run, even if there was an exception'''
        print('The finally block always runs. It is a good place to clean up')


if __name__ == '__main__':
    words = 'here is some text to be written to a file'
    d = datetime.today()
    writeOutput(str(d)) # make sure it is a string
    writeChunks(words)


