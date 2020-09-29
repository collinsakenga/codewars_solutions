def count_deaf_rats(town):
    town = "".join(town.split())
    index = town.index("P")
    total = 0
    left = town[:index]
    right = town[index+1:]
    for i in range(0, len(left), 2):
        if left[i:i+2] != "~O":
            total += 1
    for i in range(0, len(right), 2):
        if right[i:i+2] != "O~":
            total += 1
    return total
