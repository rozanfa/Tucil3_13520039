from fileReader import readPuzzleFromFile
from puzzleSolver import solvePuzzle

# [3, 1, 2, 4, 16, 5, 7, 8, 10, 6, 11, 12, 9, 13, 14, 15]
# [1, 2, 3, 4, 5, 6, 16, 8, 9, 10, 7, 11, 13, 14, 15, 12] ppt pak rin
# [7, 2, 11, 10, 15, 12, 16, 5, 9, 14, 13, 1, 3, 6, 8, 4]
# [1, 3, 5, 15, 2, 16, 5, 12, 7, 6, 11, 14, 8, 9, 10, 13]

import sys

if len(sys.argv) < 2:
    p = readPuzzleFromFile("puzzle9.txt")
else:
    p = readPuzzleFromFile(sys.argv[1])

#sys.stdout = open("output.txt", "w")
solvePuzzle(p)


'''

p = Puzzle([3, 1, 2, 4, 16, 5, 7, 8, 10, 6, 11, 12, 9, 13, 14, 15])
q = Puzzle([3, 1, 2, 4, 16, 5, 7, 8, 10, 6, 11, 12, 9, 13, 14, 15])

puzzleHistoryList = [q]
print(nodeIsInHistory(p))

'''