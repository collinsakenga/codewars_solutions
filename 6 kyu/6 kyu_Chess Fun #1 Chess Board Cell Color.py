def digitsum(s):
    total = 0
    for i in s:
        total += int(i)
    return total


def chess_board_cell_color(cell1, cell2):
    trans = str.maketrans("ABCDEFGH", "12345678")
    return digitsum(cell1.translate(trans)) % 2 == digitsum(cell2.translate(trans)) % 2
