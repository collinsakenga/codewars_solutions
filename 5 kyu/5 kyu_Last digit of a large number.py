sequence_2=[2,4,8,6]
sequence_3=[3,9,7,1]
sequence_4=[4,6]
sequence_5=[5]
sequence_6=[6]
sequence_7=[7,9,3,1]
sequence_8=[8,4,2,6]
sequence_9=[9,1]
def last_digit(n1, n2):
    if n2==0: return 1
    remainder=n1%10
    if remainder==1:
        return 1
    elif remainder==2:
        return sequence_2[n2%4-1] if n2%4!=0 else sequence_2[3]
    elif remainder==3:
        return sequence_3[n2%4-1] if n2%4!=0 else sequence_3[3]
    elif remainder==4:
        return sequence_4[n2%2-1] if n2%2!=0 else sequence_4[1]
    elif remainder==5:
        return 5
    elif remainder==6:
        return 6
    elif remainder==7:
        return sequence_7[n2%4-1] if n2%4!=0 else sequence_7[3]
    elif remainder==8:
        return sequence_8[n2%4-1] if n2%4!=0 else sequence_8[3]
    elif remainder==9:
        return sequence_9[n2%2-1] if n2%2!=0 else sequence_9[1]
    return 0