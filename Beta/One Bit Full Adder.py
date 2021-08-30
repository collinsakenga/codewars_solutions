def one_bit_full_adder(cin, a, b): 
    num=cin+a+b
    return (num//2, num%2)