def number_length(a):
    if a<10:
        return 1
    return 1+number_length(a//10)