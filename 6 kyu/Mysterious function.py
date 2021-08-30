def get_num(n):
    return sum(2 if i=="8" else 1 if (i=="6" or i=="9" or i=="0") else 0 for i in str(n))
