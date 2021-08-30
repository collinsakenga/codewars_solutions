def count_zeros_n_double_fact(n): 
    if n%2!=0:
        return 0
    multiply=10
    total=0
    while multiply<n:
        total+=n//multiply
        multiply*=5
    return total