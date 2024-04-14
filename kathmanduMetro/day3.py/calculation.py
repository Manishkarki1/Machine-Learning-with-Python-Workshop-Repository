def calculate(a,b,op):
    # it will show in the hover of calling function
    '''
    import from calculation
    '''
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        return a/b
    else:
        return "Wrong operator"


'''
def fun1(a,nonargument,keywordword) this flow should be maintain
'''
def fun1(a,*args,**kwargs):
    total=0
    for i in args:
        total=total+i;
    print(total)

