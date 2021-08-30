def ordinal(number, brief=False):
    return {11:"th", 12:"th", 13:"th"}.get(int(str(number)[-2:]), {1:"st", 2:"d" if brief else "nd", 3:"d" if brief else "rd"}.get(number%10, "th"))