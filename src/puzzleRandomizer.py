import random
from Puzzle import Puzzle

# Membuat puzzle secara acak
def getRandomPuzzle():
    # Definisikan puzzle yang sudah diselesaikan
    p = Puzzle([i+1 for i in range(16)])
    count = 0

    # Acak acak puzzle
    for i in range(30):
        r = random.randint(1,5)
        if (r == 1 or r == 5) and p.blankUbin > 3 and p.getLastStep() != "U":
            p.swapUp()
            count += 1
        if r == 2 and p.blankUbin < 12 and p.getLastStep() != "D":
            p.swapDown()
            count += 1
        if r == 3 and p.blankUbin % 4 != 3 and p.getLastStep() != "R":
            try:
                p.swapRight()
                count += 1
            except:
                pass
        if r == 4 and p.blankUbin % 4 != 0 and p.getLastStep() != "L":
            try:
                p.swapLeft()
                count += 1
            except:
                pass
        p.print()
    
    # Masukkan puzzle ke list
    arr = []
    for i in range(16):
        arr.append(p.ubin[i].value)
    return arr