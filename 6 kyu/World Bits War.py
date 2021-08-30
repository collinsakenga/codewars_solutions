def bits_war(numbers):
    odd=even=0
    for i in numbers:
        if i%2==0:
            even+=bin(i)[2:].count("1") if i>0 else -bin(abs(i))[2:].count("1")
        else:
            odd+=bin(i)[2:].count("1") if i>0 else -bin(abs(i))[2:].count("1")
    return "odds win" if odd>even else "evens win" if even>odd else "tie"