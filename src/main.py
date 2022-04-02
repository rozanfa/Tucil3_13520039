from fileReader import readPuzzleFromFile
from puzzleSolver import solvePuzzle
from puzzleRandomizer import getRandomPuzzle
import sys
import os

# Pindah direktori ke parent-nya
os.chdir("..")

# Buat string path ke folder test
path = os.getcwd() + "\\test\\"

# Cek apakah tidak terdapat argumen
if len(sys.argv) < 2:
    print("1. Input dari file")
    print("2. Input dari CLI")
    print("3. Dapatkan puzzle secara acak")
    pilihan = input("Pilihan: ")
    print()

    if pilihan == "1": # Input dari file
        print("(File harus berada di dalam folder test)")
        fileName = input("Nama file: ")
        p = readPuzzleFromFile(path + fileName)

    elif pilihan == "2": # Input dari CLI
        p = []
        for i in range(16):
            p.append(int(input(f"Ubin {i+1}: ")))

    elif pilihan == "3": # Dapatkan puzzle secara acak
        p = getRandomPuzzle()

    else: # Input tidak valid
        print("Pilihan tidak valid")
        exit()

else:
    p = readPuzzleFromFile(path + sys.argv[1])

solvePuzzle(p)