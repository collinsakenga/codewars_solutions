def is_it_possible(field):
    count_X=field.count("X")
    count_0=field.count("0")
    if abs(count_X-count_0)>=2 or count_0>count_X:
        return False
    if possible(field, "X") and possible(field, "0"):
        return False
    elif possible(field, "X") and count_X==count_0:
        return False
    elif possible(field, "0") and count_X!=count_0:
        return False
    return True
def possible(table, sign):
    if table[0]==table[4]==table[8]==sign or table[2]==table[4]==table[6]==sign:
        return True
    elif any(table[i:i+3]==sign*3 for i in range(0, len(table), 3)) or any((table[i]+table[3+i]+table[6+i])==sign*3 for i in range(3)):
        return True
    return False