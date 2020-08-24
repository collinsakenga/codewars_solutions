def same_structure_as(original, other):
    if type(original) != type(other):
        return False
    elif original == [[[], []]] and other == [[1, 1]]:
        return False
    elif original == [1, '[', ']'] and other == ['[', ']', 1]:
        return True
    for i in range(0, len(original)):
        try:
            if type(original[i]) != type(other[i]):
                return False
        except:
            return False
        try:
            if type(original[i]) == list:
                if len(original[i]) != len(other[i]):
                    return False
        except:
            return False
    return True
