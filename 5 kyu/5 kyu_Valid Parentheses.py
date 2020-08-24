def valid_parentheses(string):
    result = [char for char in string if char in "()"]
    comp = -1
    total = len(result)
    if len(result) % 2 == 1:
        return False
    index = 0
    while True:
        if total == 0:
            return True
        if index >= total-1:
            index = 0
            total = len(result)
            if comp == total:
                return False
            comp = total
        if result[index+1] == ")" and result[index] == "(":
            del result[index:index+2]
            total -= 2
        index += 1
