# we can use number formatting in our print output

def showApproxAnswer(a,b,op):
    '''calculate and and b with the operator
       then show the result to 2dp'''
    if op=='+':
        result = a+b
    elif op=='/':
        result = a/b
    elif op=='*':
        result = a*b
    # return the answer to 2 decimal places (as a floating point value)
    return '{:0.2f}'.format(result)
    

if __name__ == '__main__':
    print( showApproxAnswer(1,2,'+') )
    print( showApproxAnswer(9,2,'/') )
    print( showApproxAnswer(4,3,'*') )