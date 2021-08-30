def max_consec_zeros(n):
    num2words= {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen'}
    n="{:b}".format(int(n))
    count_zero=0
    comp=0
    for zero in str(n):
        if zero=='0':
            count_zero+=1
        else:
            count_zero=0
        if count_zero>comp:
            comp=count_zero
    return num2words[comp]