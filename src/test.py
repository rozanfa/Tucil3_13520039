from tkinter import *
from SolvedPuzzle import SolvedPuzzle 
from fileReader import readPuzzleFromFile
from puzzleSolver import getSolvedPuzzle, solvePuzzle
from Puzzle import Puzzle
from puzzleRandomizer import getRandomPuzzle
import time
from tkinter import filedialog as fd
  
top = Tk()   
top.geometry("500x300")
top.minsize(500,300)
top.maxsize(500,300)  
p = None
puzzle = None
timeElapsed = None

def hide_component(component):
    component.pack_forget()

def show_component(component):
    component.pack()


def initialize(puzzleInput):
    global puzzle
    puzzle = None
    puzzle = puzzleInput
    global p
    puzzleObject = None
    puzzleObject = Puzzle(puzzle)
    arr = puzzleObject.toStringList()
    label1.config(text = arr[0])
    label2.config(text = arr[1])
    label3.config(text = arr[2])
    label4.config(text = arr[3])
    label5.config(text = arr[4])
    label6.config(text = arr[5])
    label7.config(text = arr[6])
    label8.config(text = arr[7])
    label9.config(text = arr[8])
    label10.config(text = arr[9])
    label11.config(text = arr[10])
    label12.config(text = arr[11])
    label13.config(text = arr[12])
    label14.config(text = arr[13])
    label15.config(text = arr[14])
    label16.config(text = arr[15])


    kurangList = puzzleObject.getKurangList()
    kurang_1.config(text = f"KURANG(1) = {kurangList[0]}")
    kurang_2.config(text = f"KURANG(2) = {kurangList[1]}")
    kurang_3.config(text = f"KURANG(3) = {kurangList[2]}")
    kurang_4.config(text = f"KURANG(4) = {kurangList[3]}")
    kurang_5.config(text = f"KURANG(5) = {kurangList[4]}")
    kurang_6.config(text = f"KURANG(6) = {kurangList[5]}")
    kurang_7.config(text = f"KURANG(7) = {kurangList[6]}")
    kurang_8.config(text = f"KURANG(8) = {kurangList[7]}")
    kurang_9.config(text = f"KURANG(9) = {kurangList[8]}")
    kurang_10.config(text = f"KURANG(10) = {kurangList[9]}")
    kurang_11.config(text = f"KURANG(11) = {kurangList[10]}")
    kurang_12.config(text = f"KURANG(12) = {kurangList[11]}")
    kurang_13.config(text = f"KURANG(13) = {kurangList[12]}")
    kurang_14.config(text = f"KURANG(14) = {kurangList[13]}")
    kurang_15.config(text = f"KURANG(15) = {kurangList[14]}")
    kurang_16.config(text = f"KURANG(16) = {kurangList[15]}")
    X = puzzleObject.checkX()
    print(X)
    X_label.config(text = f"X = {X}")
    sumOfKurangValue = puzzleObject.sumOfKurang
    sum_of_kurang.config(text = f"SUM(KURANG) + X = {sumOfKurangValue + X}")
    if (sumOfKurangValue + X) % 2 == 0:
        bSolvePuzzle.config(state=ACTIVE)
        lPuzzleCanBeSolved.config(text = "Puzzle can be solved")
    else :
        bSolvePuzzle.config(state=DISABLED)
        lPuzzleCanBeSolved.config(text = "Puzzle can't be solved")
    lPleaseWait.config(text = "Please click and wait...")
    lTimeElapsed.config(text = "")

    

def chooseFile():
    global p
    global puzzle
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    bSolvePuzzle.config(state=DISABLED)
    p = None
    puzzle = None
    filename = None
    filename = fd.askopenfilename()
    initialize(readPuzzleFromFile(filename))
    bSolvePuzzle.config(state=ACTIVE)
    
    bAnimate.config(state=DISABLED)

def getRandom():
    global p
    global puzzle
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    bSolvePuzzle.config(state=DISABLED)
    p = None
    puzzle = None
    initialize(getRandomPuzzle())
    bSolvePuzzle.config(state=ACTIVE)
    

def showPleaseWait():
    lPleaseWait.config(text = "Please wait...")

def hidePleaseWait():
    lPleaseWait.config(text = "Complete!")


def solvePuzzle():
    showPleaseWait()
    global p
    global puzzle
    global timeElapsed
    top.after(1000, lambda: showPleaseWait())
    p = None
    p, timeElapsed = getSolvedPuzzle(puzzle)
    b1.config(state=ACTIVE)
    b2.config(state=ACTIVE)
    bAnimate.config(state=ACTIVE)
    top.after(1000, lambda: hidePleaseWait())
    hidePleaseWait()
    lTimeElapsed.config(text = "Time elapsed: {:.5f}".format(timeElapsed))


def putInLabel():
    global p
    arr = p.toStringList()
    label1.config(text = arr[0])
    label2.config(text = arr[1])
    label3.config(text = arr[2])
    label4.config(text = arr[3])
    label5.config(text = arr[4])
    label6.config(text = arr[5])
    label7.config(text = arr[6])
    label8.config(text = arr[7])
    label9.config(text = arr[8])
    label10.config(text = arr[9])
    label11.config(text = arr[10])
    label12.config(text = arr[11])
    label13.config(text = arr[12])
    label14.config(text = arr[13])
    label15.config(text = arr[14])
    label16.config(text = arr[15])


def next():
    global p
    p.nextStep()
    arr = p.toStringList()
    label1.config(text = arr[0])
    label2.config(text = arr[1])
    label3.config(text = arr[2])
    label4.config(text = arr[3])
    label5.config(text = arr[4])
    label6.config(text = arr[5])
    label7.config(text = arr[6])
    label8.config(text = arr[7])
    label9.config(text = arr[8])
    label10.config(text = arr[9])
    label11.config(text = arr[10])
    label12.config(text = arr[11])
    label13.config(text = arr[12])
    label14.config(text = arr[13])
    label15.config(text = arr[14])
    label16.config(text = arr[15])
    if p.state == p.stepsCount:
        stateLabel.config(text = "Final State")
    else:
        stateLabel.config(text = "State: " + str(p.state))
    
def prev():
    global p
    p.prevStep()
    arr = p.toStringList()
    label1.config(text = arr[0])
    label2.config(text = arr[1])
    label3.config(text = arr[2])
    label4.config(text = arr[3])
    label5.config(text = arr[4])
    label6.config(text = arr[5])
    label7.config(text = arr[6])
    label8.config(text = arr[7])
    label9.config(text = arr[8])
    label10.config(text = arr[9])
    label11.config(text = arr[10])
    label12.config(text = arr[11])
    label13.config(text = arr[12])
    label14.config(text = arr[13])
    label15.config(text = arr[14])
    label16.config(text = arr[15])
    if p.state == 0:
        stateLabel.config(text = "Initial State")
    else:
        stateLabel.config(text = "State: " + str(p.state))

def animatePuzzle():
    global p
    p = SolvedPuzzle(puzzle, p.steps)
    for i in range(p.stepsCount + 1):
        if i == 0:
            top.after(i * 500, lambda: putInLabel())
        else:
            top.after(i * 500, lambda: next())



puzzleFrame = Frame(top, width = 200, height = 250)
puzzleFrame.place(x = 300, y = 90)
label1 = Label(puzzleFrame, text = " 1")
label2 = Label(puzzleFrame, text = " 2")
label3 = Label(puzzleFrame, text = " 3")
label4 = Label(puzzleFrame, text = " 4") 
label5 = Label(puzzleFrame, text = " 5")
label6 = Label(puzzleFrame, text = " 6")
label7 = Label(puzzleFrame, text = " 7")
label8 = Label(puzzleFrame, text = " 8") 
label9 = Label(puzzleFrame, text = " 9")
label10 = Label(puzzleFrame, text = "10")  
label11 = Label(puzzleFrame, text = "11")
label12 = Label(puzzleFrame, text = "12")
label13 = Label(puzzleFrame, text = "13")
label14 = Label(puzzleFrame, text = "14")
label15 = Label(puzzleFrame, text = "15")
label16 = Label(puzzleFrame, text = "  ")



label1.place(x = 40, y = 40)  
label2.place(x = 60, y = 40)  
label3.place(x = 80, y = 40)  
label4.place(x = 100, y = 40)  
label5.place(x = 40, y = 60)  
label6.place(x = 60, y = 60)  
label7.place(x = 80, y = 60)  
label8.place(x = 100, y = 60)  
label9.place(x = 40, y = 80)  
label10.place(x = 60, y = 80)  
label11.place(x = 80, y = 80)  
label12.place(x = 100, y = 80)  
label13.place(x = 40, y = 100)  
label14.place(x = 60, y = 100)  
label15.place(x = 80, y = 100)  
label16.place(x = 100, y = 100)  
    
b1 = Button(puzzleFrame, text = "Next", command = next)
b1.place(x = 100, y = 10)
b1.config(state = DISABLED)

b2 = Button(puzzleFrame, text = "Prev", command = prev)
b2.place(x = 20, y = 10)
b2.config(state = DISABLED)

stateLabel = Label(puzzleFrame, text = "Initial state")
stateLabel.place(x = 20, y = 120)


leftFrame = Frame(top, width = 300, height = 260)
leftFrame.place(x = 20, y = 20)

bOpenPuzzle = Button(leftFrame, text = "Open Puzzle", command = chooseFile)
bGetRandom = Button(leftFrame, text = "Get Random Puzzle", command = getRandom)
bOpenPuzzle.place(x = 0, y = 0)
bGetRandom.place(x = 100, y = 0)
kurang_1 = Label(leftFrame, text = " ")
kurang_1.place(x = 0, y = 30)
kurang_2 = Label(leftFrame, text = " ")
kurang_2.place(x = 0, y = 50)
kurang_3 = Label(leftFrame, text = " ")
kurang_3.place(x = 0, y = 70)
kurang_4 = Label(leftFrame, text = " ")
kurang_4.place(x = 0, y = 90)
kurang_5 = Label(leftFrame, text = " ")
kurang_5.place(x = 0, y = 110)
kurang_6 = Label(leftFrame, text = " ")
kurang_6.place(x = 0, y = 130)
kurang_7 = Label(leftFrame, text = " ")
kurang_7.place(x = 0, y = 150)
kurang_8 = Label(leftFrame, text = " ")
kurang_8.place(x = 0, y = 170)
kurang_9 = Label(leftFrame, text = " ")
kurang_9.place(x = 100, y = 30)
kurang_10 = Label(leftFrame, text = " ")
kurang_10.place(x = 100, y = 50)
kurang_11 = Label(leftFrame, text = " ")
kurang_11.place(x = 100, y = 70)
kurang_12 = Label(leftFrame, text = " ")
kurang_12.place(x = 100, y = 90)
kurang_13 = Label(leftFrame, text = " ")
kurang_13.place(x = 100, y = 110)
kurang_14 = Label(leftFrame, text = " ")
kurang_14.place(x = 100, y = 130)
kurang_15 = Label(leftFrame, text = " ")
kurang_15.place(x = 100, y = 150)
kurang_16 = Label(leftFrame, text = " ")
kurang_16.place(x = 100, y = 170)
X_label = Label(leftFrame, text = " ")
X_label.place(x = 20, y = 200)
sum_of_kurang = Label(leftFrame, text = " ")
sum_of_kurang.place(x = 20, y = 220)

lPuzzleCanBeSolved = Label(leftFrame, text = "Choose a puzzle first")
lPuzzleCanBeSolved.place(x = 20, y = 240)

bSolvePuzzle = Button(top, text = "Solve Puzzle", command = solvePuzzle, state=DISABLED)
bSolvePuzzle.place(x = 340, y = 40)

bAnimate = Button(top, text = "Animate", command = animatePuzzle, state=DISABLED)
bAnimate.place(x = 350, y = 240)

lPleaseWait = Label(top, text = "Choose a puzzle first")
lPleaseWait.place(x = 340, y = 70)


lTimeElapsed = Label(leftFrame, text = "")
lTimeElapsed.place(x = 175, y = 240)

top.mainloop() 