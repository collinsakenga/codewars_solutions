def encode(testing):
    for i in range(len(testing)):
        if testing[i]=='a':
            testing=testing[:i]+'1'+testing[i+1:]
        elif testing[i]=='e':
            testing=testing[:i]+'2'+testing[i+1:]
        elif testing[i]=='i':
            testing=testing[:i]+'3'+testing[i+1:]
        elif testing[i]=='o':
            testing=testing[:i]+'4'+testing[i+1:]
        elif testing[i]=='u':
            testing=testing[:i]+'5'+testing[i+1:]
    return testing
    
def decode(testing):
    for i in range(len(testing)):
        if testing[i]=='1':
            testing=testing[:i]+'a'+testing[i+1:]
        elif testing[i]=='2':
            testing=testing[:i]+'e'+testing[i+1:]
        elif testing[i]=='3':
            testing=testing[:i]+'i'+testing[i+1:]
        elif testing[i]=='4':
            testing=testing[:i]+'o'+testing[i+1:]
        elif testing[i]=='5':
            testing=testing[:i]+'u'+testing[i+1:]
    return testing