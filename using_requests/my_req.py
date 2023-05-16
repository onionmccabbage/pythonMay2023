import sys

# we can use the requests library to make API calls over http(s)
# API is Application Programming Interface
# often called REST or RESTful
# REpresent STate on a URL

# NB older Python used urllib for requests
# that still exists but is more long-winded and needs more code to make it work

import requests # remember we may need to pip install requests

def makeCall(n=1): # n has a sensible default value
    '''Here we will make a call for some JSON text
       retrieve whichever single user is specified'''
    url = f'https://jsonplaceholder.typicode.com/users/{n}' # we append the number
    response = requests.get(url) # here we get a response from the API server
    # if the API returns text
    # response_txt = response.text()
    # if the API returns HTML
    # response_html = response.html()
    # if the API returns xml
    # response_xml = response.xml()
    # since we know the API will return JSON we can just read the JSON from the response
    response_l = response.json() # Python will automatically convert the JSON to a structure
    return response_l

if __name__ == '__main__':
    # check if there is an additional system argument valriable
    # if there is, validate it is an integer, then use it in the request call
    a=1
    if len(sys.argv)>1: # remember sys.argv[0] is always the module name
        a = int(float(sys.argv[1]))# all sys.argv are STRING!!!
        if type(a)==int and 1<=a<=10: # or 0<a<11
            pass # just use the value 
        else:
            a=1
    users = makeCall(a) # we can override the default value of 1
    # if we have just one user we can prnt the values nicely
    print( type(users) )
    # use triple quotes so we can have new lines in our string
    print(f'''User {users["name"]} lives at {users["address"]["street"]}
lat: {users["address"]["geo"]["lat"]} lng: {users["address"]["geo"]["lng"]}''')
    # if we have more than one user, we can iterate over the list (it is a list of dictionaries)
    # for user in users:
    #     print( f'User {user["name"]} email {user["email"]} lives at {user["address"]["street"]}' )