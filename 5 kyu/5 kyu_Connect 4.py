class Connect4():
    def __init__(self):
        self.grid = [[" "]*7 for i in range(6)]
        self.check = [0]*7
        self.player = False
        self.finish = False

    def play(self, col):
        if self.finish:
            return "Game has finished!"
        self.check[col] += 1
        if self.check[col] >= 7:
            return "Column full!"
        self.player = not self.player
        self.grid[6-self.check[col]][col] = "O" if self.player else "X"
        self.print_grid()
        if self.solve():
            self.finish = True
            return "Player 1 wins!" if self.player else "Player 2 wins!"
        return "Player 1 has a turn" if self.player else "Player 2 has a turn"

    def solve(self):
        for i in range(0, 6):
            for j in range(0, 4):
                if (self.grid[i][j] == self.grid[i][j+1] == self.grid[i][j+2] == self.grid[i][j+3]):
                    if (self.grid[i][j] != " "):
                        return True
        for i in range(0, 7):
            for j in range(0, 3):
                if (self.grid[j][i] == self.grid[j+1][i] == self.grid[j+2][i] == self.grid[j+3][i]):
                    if (self.grid[j][i] != " "):
                        return True
        for i in range(0, 3):
            for j in range(0, 4):
                if (self.grid[i][j] == self.grid[i+1][j+1] == self.grid[i+2][j+2] == self.grid[i+3][j+3]):
                    if (self.grid[i][j] != " "):
                        return True
        for i in range(5, 2, -1):
            for j in range(0, 4):
                if (self.grid[i][j] == self.grid[i-1][j+1] == self.grid[i-2][j+2] == self.grid[i-3][j+3]):
                    if (self.grid[i][j] != " "):
                        return True
        return False

    def print_grid(self):
        for i in self.grid:
            for j in i:
                print("_"+j, end="")
            print()
