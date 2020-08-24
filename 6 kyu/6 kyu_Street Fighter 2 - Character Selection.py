def street_fighter_selection(fighters, initial_position, moves):
    row = len(fighters)
    col = len(fighters[0])
    result = []
    y = initial_position[0]
    x = initial_position[1]
    for move in moves:
        if move == "up":
            if y != 0:
                y -= 1
            result.append(fighters[y][x])
        elif move == "down":
            if y != row-1:
                y += 1
            result.append(fighters[y][x])
        elif move == "right":
            if x == col-1:
                x = 0
            else:
                x += 1
            result.append(fighters[y][x])
        elif move == "left":
            if x == 0:
                x = col-1
            else:
                x -= 1
            result.append(fighters[y][x])
    return result
