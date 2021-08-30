def is_rotation(s1,s2):
    for i in range(len(s1)):
        s1=s1[1:]+s1[0]
        if s1==s2:
            return True
    return False if s1!=s2 else True