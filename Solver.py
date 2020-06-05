from Sudoku import Sudoku
from time import sleep


class Solver():

    def __init__(self, sudoku_grid: Sudoku, delay=0.0, showsteps = False):
        self.delay = delay
        self.showsteps = showsteps
        self.sudoku = sudoku_grid
        self.grid = self.sudoku.getGrid()
        self.poss = set() # it will store the possibilities for one case
        self.steps = 0
        self.solver()

    def checkLines(self):
        cpt = 0
        for i in range(9):
            tmp = set(self.grid[i])
            if len(tmp) == 9:
                cpt += 1
        return cpt == 9

    def checkColumns(self):
        cpt = 0
        for i in range(9):
            tmp = set()
            for j in range(9):
                tmp.add(self.grid[j][i])
            if len(tmp) == 9:
                cpt += 1
        return cpt == 9

    def checkOneSquare(self, i, j):
        tmp = set()
        for x in range(3):
            for y in range(3):
                tmp.add(self.grid[i+x][j+y])
        return len(tmp) == 9 and 0 not in tmp

    def checkSquares(self):
        cpt = 0
        for x in range(3):
            for y in range(3):
                if(self.checkOneSquare(x*3, y*3)):
                    cpt += 1
        return cpt == 9

    def isFinished(self):
        return self.checkLines() and self.checkColumns() and self.checkSquares()

    def getFirstEmptyCase(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return(i, j)

    def changeCase(self, x, y, value):
        self.grid[x][y] = value
        self.steps += 1
        if self.showsteps:
            sleep(self.delay)
            print(str.format("============================ Step n° {} ============================", self.steps))
            self.sudoku.displayGrid()

    def removePossibility(self, number):
        if number in self.poss:
            self.poss.remove(number)

    def getPossibilitiesForCase(self, x, y):
        self.poss = {x for x in range(1, 10)}
        self.removeLinePossibilities(x)
        self.removeColPossibilities(y)
        self.removeSquarePossibilities(x, y)
        return self.poss

    def removeLinePossibilities(self, x):
        for y in range(9):
            self.removePossibility(self.grid[x][y])

    def removeColPossibilities(self, y):
        for x in range(9):
            self.removePossibility(self.grid[x][y])

    def removeSquarePossibilities(self, x, y):
        x = x - x % 3
        y = y - y % 3
        for i in range(3):
            for j in range(3):
                self.removePossibility(self.grid[x+i][y+j])

    def solver(self):
        if self.isFinished():
            return True
        else:
            x, y = self.getFirstEmptyCase()
            poss = self.getPossibilitiesForCase(x, y)
            if len(poss) == 0:
                return False
            else:
                for elem in poss:
                    self.changeCase(x, y, elem)
                    if self.solver():
                        return True
                    self.changeCase(x, y, 0)
