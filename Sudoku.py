class Sudoku():

    def __init__(self, g):
        self.grid = [[int(g[i*9+j]) for j in range(9)] for i in range(9)]

    def getGrid(self):
        return self.grid

    def displayCase(self, i, j):
        if self.grid[i][j] == 0:
            return "."
        return self.grid[i][j]

    def displayGrid(self):
        l = "---"*10+"-"
        for i in range(9):
            if((i)%3==0):
                print(l)
            print(str.format("| {}  {}  {} | {}  {}  {} | {}  {}  {} |",
                  self.displayCase(i, 0), self.displayCase(i, 1), self.displayCase(i, 2),
                  self.displayCase(i, 3), self.displayCase(i, 4), self.displayCase(i, 5),
                  self.displayCase(i, 6), self.displayCase(i, 7), self.displayCase(i, 8)))
        print(l)
