def tops(msg):
    count = 2
    start = 2
    increment = 7
    solution = ""
    while True:
        if start >= len(msg):
            return solution
        solution = msg[start:start+count]+solution
        start += increment
        count += 1
        increment += 4
