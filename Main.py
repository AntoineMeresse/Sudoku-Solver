from Sudoku import Sudoku
from Solver import Solver
import sys
from time import time

def main(args):
    cpt = 0
    t1 = time()
    with open("datas/sudoku5000", "r") as fl:
        grids = fl.readlines()
        for g in grids:
            s = Sudoku(g.split(":")[1])
            Solver(s)
            cpt +=1
            #print(str.format("{} grids solved.", cpt))
    t2 = time()
    print(str.format("==> {} sudoku grids has been solved in {} seconds.", len(grids), t2-t1))


if __name__ == "__main__":
    main(sys.argv)