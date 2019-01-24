import random


class Minesweeper(object):

    def __init__(self, row=30, col=24, num_mines=100):
        self.grid = [[1]*col for _ in range(row)]
        self.hidden_grid = [[-1]*col for _ in range(row)]
        self.num_mines = num_mines
        self.num_selectable_spots = 720 - num_mines
        self.gameOver = False
        self.setup()

    def setup(self):
        print("Setting up grid")
        print(len(self.grid))
        print(len(self.grid[0]))
        i = 0
        while i < self.num_mines:
            self.putMineOnGrid()
            i += 1
        print("Done setting up grid")

    def putMineOnGrid(self):
        random_int = random.randint(0, 719)
        rand_x = int(random_int / 24)
        rand_y = int(random_int % 24)
        while self.grid[rand_x][rand_y] == -2 or (rand_x == 0 and rand_y == 0):
            random_int = random.randint(0, 719)
            rand_x = int(random_int / 24)
            rand_y = int(random_int % 24)
        self.grid[rand_x][rand_y] = -2

    def pickSpot(self, x, y):

        if self.grid[y][x] == 1:
            self.reveal_adjacent_squares(y, x)

        elif self.grid[x][y] == -2:
            self.gameOver = True
            print("You Lose")

    def reveal_adjacent_squares(self, x, y):
        countNumAdjacentMines = 0

        if x-1 >= 0 and self.grid[x-1][y] == 1:
            self.hidden_grid[x-1][y] = 0
            self.num_selectable_spots -= 1
        elif x-1 >= 0:
            countNumAdjacentMines += 1

        if x+1 < len(self.grid) and self.grid[x+1][y] == 1:
            self.hidden_grid[x+1][y] = 0
            self.num_selectable_spots -= 1
        elif x+1 < len(self.grid):
            countNumAdjacentMines += 1

        if y-1 >= 0 and self.grid[x][y-1] == 1:
            self.hidden_grid[x][y-1] = 0
            self.num_selectable_spots -= 1
        elif y-1 >= 0:
            countNumAdjacentMines += 1

        if y+1 < len(self.grid[x]) and self.grid[x][y+1] == 1:
            self.hidden_grid[x][y+1] = 0
            self.num_selectable_spots -= 1
        elif y+1 < len(self.grid[x]):
            countNumAdjacentMines += 1

        self.hidden_grid[x][y] = countNumAdjacentMines
        if self.num_selectable_spots == 0:
            self.gameOver = True

    def play_game(self):
        self.gameOver = False
        while not self.gameOver:
            print("Input your X and Y")
            x = int(input("X: "))
            y = int(input("Y: "))
            self.pickSpot(x, y)
            if not self.gameOver:
                self.print_board()

    def print_board(self):
        for row in self.hidden_grid:
            print(row)


minesweeper = Minesweeper()
minesweeper.play_game()
