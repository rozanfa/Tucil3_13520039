import copy
from Puzzle import Puzzle
from SolvedPuzzle import SolvedPuzzle
import time

puzzleList = []
puzzleHistoryList = []
puzzleHistoryMap = {}
found = False
result = None
nodeCount = 0

# Mengecek apakah dua ubin bernilai sama
def checkIfUbinIsEqual(ubin1, ubin2):
    for i in range(16):
        if ubin1[i].value != ubin2[i].value:
            return False
    return True

# Mengecek apakah node sudah pernah ada
def nodeIsInHistory(node):
    global puzzleHistoryList
    for i in range(len(puzzleHistoryList)):
        if checkIfUbinIsEqual(puzzleHistoryList[i].ubin, node.ubin):
            return True
    return False

def nodeIdIsInHistoryMap(puzzle):
    global puzzleHistoryMap
    id = puzzle.toPuzzleId()
    return id in puzzleHistoryMap

# Mengeksekusi node
def executeNode(puzzle):
    global puzzleList
    global puzzleHistoryMap
    global found
    global result
    global nodeCount
    if puzzle.countNotInRightPlace() == 0:  # Jika sudah ketemu
        found = True
        result = puzzle
    else:   # Bangkitkan simpul anak
        if puzzle.blankUbin % 4 != 3 and puzzle.getLastStep() != "R":
            swapRightPuzzle = copy.deepcopy(puzzle)
            swapRightPuzzle.swapRight()
            if not nodeIdIsInHistoryMap(swapRightPuzzle):
                puzzleList.append(swapRightPuzzle)
                puzzleHistoryMap[swapRightPuzzle.toPuzzleId()] = True
                nodeCount += 1
        if puzzle.blankUbin % 4 != 0 and puzzle.getLastStep() != "L":
            swapLeftPuzzle = copy.deepcopy(puzzle)
            swapLeftPuzzle.swapLeft()
            if not nodeIdIsInHistoryMap(swapLeftPuzzle):
                puzzleList.append(swapLeftPuzzle)
                puzzleHistoryMap[swapLeftPuzzle.toPuzzleId()] = True
                nodeCount += 1
        if puzzle.blankUbin < 12 and puzzle.getLastStep() != "D":
            swapDownPuzzle = copy.deepcopy(puzzle)
            swapDownPuzzle.swapDown()
            if not nodeIdIsInHistoryMap(swapDownPuzzle):
                puzzleList.append(swapDownPuzzle)
                puzzleHistoryMap[swapDownPuzzle.toPuzzleId()] = True
                nodeCount += 1
        if puzzle.blankUbin > 3 and puzzle.getLastStep() != "U":
            swapUpPuzzle = copy.deepcopy(puzzle)
            swapUpPuzzle.swapUp()
            if not nodeIdIsInHistoryMap(swapUpPuzzle):
                puzzleList.append(swapUpPuzzle)
                puzzleHistoryMap[swapUpPuzzle.toPuzzleId()] = True
                nodeCount += 1


# Mencari index node dengan jarak terpendek
def findShortestDistanceIndex():
    global puzzleList
    min = puzzleList[0].countNotInRightPlace() + puzzleList[0].stepsCount * 0.05
    index = 0
    for i in range(1, len(puzzleList)):
        currCost = puzzleList[i].countNotInRightPlace() + puzzleList[i].stepsCount * 0.05
        if currCost < min:
            min = currCost
            index = i
    return index
    
# Membersihkan variabel global
def clearGlobalVariable():
    global found
    global result
    global puzzleList
    global puzzleHistoryList
    puzzleList = []
    puzzleHistoryList = []
    found = False
    result = None


# Fungsi utama untuk mencari solusi puzzle
# Digunakan untuk CLI
def solvePuzzle(puzzleAwal):
    global found
    global result
    global puzzleList
    global puzzleHistoryList
    global nodeCount
    clearGlobalVariable()
    before = time.time()
    puzzle = Puzzle(puzzleAwal)
    puzzle.initializeCLI()

    # Cek apakah puzzle bisa diseelsaikan
    if (puzzle.sumOfKurang + puzzle.X) % 2 == 1:
        print("Sum of Kurang + X bernilai ganjil")
        print("Puzzle tidak dapat diselesaikan")
    else:
        print("Please wait...")

        # Masukkan puzzle awal ke dalam antrian
        puzzleList = [puzzle]

        # Eksekusi node sampai ketemu
        while len(puzzleList) > 0 and not found:
            idx = findShortestDistanceIndex()
            executeNode(puzzleList[idx])
            puzzleList.pop(idx)
        after = time.time()

        sp = SolvedPuzzle(puzzleAwal, result.steps)
        sp.printStepByStep()
        print("Node count:", nodeCount)
        print("Step count:", result.stepsCount)
        print("Time elapsed:",after-before, "seconds")

# Fungsi utama untuk mendapatkan puzzle yang sudah dipecahkan
# Digunakan untuk GUI
def getSolvedPuzzle(puzzleAwal):
    global found
    global result
    global puzzleList
    global puzzleHistoryList
    clearGlobalVariable()
    before = time.time()
    puzzle = Puzzle(puzzleAwal)
    puzzle.initializeCLI()

    # Cek apakah puzzle bisa diseelsaikan
    if (puzzle.sumOfKurang + puzzle.X) % 2 == 1:
        print("Sum of Kurang + X bernilai ganjil")
        print("Puzzle tidak dapat diselesaikan")
    else:
        print("Please wait...")

        # Masukkan puzzle awal ke dalam antrian
        puzzleList = [puzzle]

        # Eksekusi node sampai ketemu
        while len(puzzleList) > 0 and not found:
            idx = findShortestDistanceIndex()
            executeNode(puzzleList[idx])
            puzzleList.pop(idx)

        after = time.time()

        sp = SolvedPuzzle(puzzleAwal, result.steps)
        return sp, after-before


