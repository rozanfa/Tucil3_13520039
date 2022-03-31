import copy
from Puzzle import Puzzle
from SolvedPuzzle import SolvedPuzzle
import time

puzzleList = []
puzzleHistoryList = []
found = False
result = None

def checkIfUbinIsEqual(ubin1, ubin2):
    for i in range(16):
        if ubin1[i].value != ubin2[i].value:
            return False
    return True

def nodeIsInHistory(node):
    global puzzleHistoryList
    for i in range(len(puzzleHistoryList)):
        if checkIfUbinIsEqual(puzzleHistoryList[i].ubin, node.ubin):
            return True
    return False


def executeNode(puzzle):
    global puzzleList
    global found
    global result
    if puzzle.countNotInRightPlace() == 0:
        found = True
        result = puzzle
    else:
        if puzzle.blankUbin % 4 != 3 and puzzle.getLastStep() != "R":
            swapRightPuzzle = copy.deepcopy(puzzle)
            swapRightPuzzle.swapRight()
            if not nodeIsInHistory(swapRightPuzzle):
                puzzleList.append(swapRightPuzzle)
                puzzleHistoryList.append(swapRightPuzzle)
        if puzzle.blankUbin % 4 != 0 and puzzle.getLastStep() != "L":
            swapLeftPuzzle = copy.deepcopy(puzzle)
            swapLeftPuzzle.swapLeft()
            if not nodeIsInHistory(swapLeftPuzzle):
                puzzleList.append(swapLeftPuzzle)
                puzzleHistoryList.append(swapLeftPuzzle)
        if puzzle.blankUbin < 12 and puzzle.getLastStep() != "D":
            swapDownPuzzle = copy.deepcopy(puzzle)
            swapDownPuzzle.swapDown()
            if not nodeIsInHistory(swapDownPuzzle):
                puzzleList.append(swapDownPuzzle)
                puzzleHistoryList.append(swapDownPuzzle)
        if puzzle.blankUbin > 3 and puzzle.getLastStep() != "U":
            swapUpPuzzle = copy.deepcopy(puzzle)
            swapUpPuzzle.swapUp()
            if not nodeIsInHistory(swapUpPuzzle):
                puzzleList.append(swapUpPuzzle)
                puzzleHistoryList.append(swapUpPuzzle)


def findShortestDistanceIndex():
    global puzzleList
    min = puzzleList[0].countNotInRightPlace() + puzzleList[0].stepsCount * 0.10
    index = 0
    for i in range(1, len(puzzleList)):
        currCost = puzzleList[i].countNotInRightPlace() + puzzleList[i].stepsCount * 0.10
        if currCost < min:
            min = currCost
            index = i
    return index
    

def solvePuzzle(puzzleAwal):
    before = time.time()
    puzzle = Puzzle(puzzleAwal)
    if (puzzle.sumOfKurang + puzzle.X) % 2 == 1:
        print("Sum of Kurang + X bernilai genap")
        print("Puzzle tidak dapat diselesaikan")
    else:
        global puzzleList
        puzzleList = [puzzle]
        while len(puzzleList) > 0 and not found:
            #print(puzzleList)
            idx = findShortestDistanceIndex()
            #print("false =", puzzleList[idx].countNotInRightPlace())
            #puzzleList[idx].print()
            executeNode(puzzleList[idx])
            puzzleList.pop(idx)
        #result.print()
        #print(result.steps)
        after = time.time()

        sp = SolvedPuzzle(puzzleAwal, result.steps)
        sp.printStepByStep()
        print("Steps Count:", result.stepsCount)
        print("Time elapsed:",after-before, "seconds")