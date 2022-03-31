import random

# Fungsi untuk membuat puzzle secara acak
def getRandomPuzzle():
    puzzle = []

    # Gunakan random
    for i in range(16):
        r = random.randint(1, 16)
        if r not in puzzle: # Cek apakah sudah ada
            puzzle.append(r)

    # Masukkan sisa bilangan yang belum ada
    for i in range(1, 17):
        if i not in puzzle:
            puzzle.append(i)

    return puzzle
