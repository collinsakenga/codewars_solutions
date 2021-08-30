from functools import reduce
def choose_move(game_state):
    total=reduce(lambda x, y: x^y, game_state)
    return next((i, j-(j^total)) for i,j in enumerate(game_state) if j>j^total)