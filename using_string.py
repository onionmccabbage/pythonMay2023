# Python can represent text as a string of characters (immutable)

def find(long, short):
    '''This will look for sort within long, 
       returning where it is first located'''
    i = long.find(short)
    return i

def combine_words(word_list):
    result = '-'.join(word_list) # careful - the joiner comes FIRST
    return result

if __name__ == '__main__':
    sh = input('Find what? ')
    words = 'this is a long string of characters'
    locate = find(words, sh)
    print(f'The letter first occurs at position {locate}') 
    # here is a collection of words
    w_t = ('Nearly', 'done', 'for', 'today')
    w_l = list( w_t ) # take the string of words and make a list out of them
    print(w_l)
    print( combine_words(w_t) ) # we cna pass a list or a tuple