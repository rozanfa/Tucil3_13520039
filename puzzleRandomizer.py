import random

# Fungsi untuk membuat puzzle secara acak
def getRandomPuzzle():
    puzzle = []
    for i in range(16):
        r = random.randint(1, 16)
        if r not in puzzle:
            puzzle.append(r)
    for i in range(1, 17):
        if i not in puzzle:
            puzzle.append(i)
    return puzzle
