# Fungsi untuk membaca input dari file
def readPuzzleFromFile(fileName):
    f = open(fileName, "r")
    puzzle = []
    for line in f:
        line = line.strip()
        if line == "":
            continue
        puzzle.append(line)
    f.close()

    # Jika diletakkan dalam 1 baris
    if len(puzzle) == 1:
        puzzle = puzzle[0].split(" ")

    # Jika diletakkan dalam bentuk matriks
    elif len(puzzle) == 4:
        puzzle = puzzle[0].split(" ") + puzzle[1].split(" ") + puzzle[2].split(" ") + puzzle[3].split(" ")
        
    if len(puzzle) != 16:
        print("Puzzle tidak valid")
        return
    for i in range(16):
        puzzle[i] = int(puzzle[i])
    return puzzle
