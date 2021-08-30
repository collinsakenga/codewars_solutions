def to_camel_case(test):
    test2=''
    if len(test)>0:
        test2=test[0]
    for i in range(len(test)-1):
        if test[i]=='-' or test[i]=='_':
            test2+=test[i+1].upper()
        else:
            test2+=test[i+1]
    test2=test2.replace('_','')
    test2=test2.replace('-','')
    return test2