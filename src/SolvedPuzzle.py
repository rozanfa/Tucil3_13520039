from Ubin import Ubin

# Kelas untuk menyimpan puzzle yang sudah dipecahkan
class SolvedPuzzle:
    def __init__(self, listUbin, steps):
        self.steps = steps
        self.ubin = [Ubin(i) for i in listUbin]
        self.ubinAwal = [Ubin(i) for i in listUbin]

        for i in range(16):
            if listUbin[i] == 16 :
                self.blankUbin = i
                self.blankUbinAwal = i
                break
        


        self.stepsCount = len(self.steps)
        self.state = 0
        
        self.print()

    # Menukar 2 ubin
    def swap(self, i, j):
        temp = self.ubin[i]
        self.ubin[i] = self.ubin[j]
        self.ubin[j] = temp

    # Menggeser nilai dari ubin kosong ke atas
    def swapUp(self):
        topUbin = self.blankUbin - 4
        self.swap(topUbin, self.blankUbin)
        self.blankUbin = topUbin

    # Menggeser ubin kosong ke bawah
    def swapDown(self):
        bottomUbin = self.blankUbin + 4
        self.swap(bottomUbin, self.blankUbin)
        self.blankUbin = bottomUbin
    
    # Menggeser ubin kosong ke kiri
    def swapLeft(self):
        leftUbin = self.blankUbin - 1
        self.swap(leftUbin, self.blankUbin)
        self.blankUbin = leftUbin
    
    # Menggeser ubin kosong ke kanan
    def swapRight(self):
        rightUbin = self.blankUbin + 1
        self.swap(rightUbin, self.blankUbin)
        self.blankUbin = rightUbin
    
    # Mencetak puzzle langkah demi langkah
    # Digunakan untuk CLI
    def printStepByStep(self):
        for step in self.steps:
            if step == "U":
                self.swapUp()
                print("UP")
            elif step == "D":
                self.swapDown()
                print("DOWN")
            elif step == "L":
                self.swapLeft()
                print("LEFT")
            elif step == "R":
                self.swapRight()
                print("RIGHT")
            self.print()

    # Mencetak isi puzzle ke layar
    def print(self):
        for i in range(16):
            if i % 4 == 0:
                print('|', end='')
            if self.ubin[i].value == 16:
                print("  ", end='|')
            else:
                print(str(self.ubin[i].value).rjust(2, ' '), end='|')
            if i % 4 == 3:
                print()
        print()

    # Mengembalikan isi dari puzzle dalam bentuk list of string
    def toStringList(self):
        list = []
        for i in range(16):
            list.append(str(self.ubin[i].value if self.ubin[i].value != 16 else " ").rjust(2, ' '))
        return list

    # Pergi ke state selanjutnya
    def nextStep(self):
        if self.state < self.stepsCount:
            if self.steps[self.state] == "U":
                self.swapUp()
            elif self.steps[self.state] == "D":
                self.swapDown()
            elif self.steps[self.state] == "L":
                self.swapLeft()
            elif self.steps[self.state] == "R":
                self.swapRight()
            self.state += 1
    
    # Pergi ke state sebelumnya
    def prevStep(self):
        if self.state > 0:
            if self.steps[self.state-1] == "U":
                self.swapDown()
            elif self.steps[self.state-1] == "D":
                self.swapUp()
            elif self.steps[self.state-1] == "L":
                self.swapRight()
            elif self.steps[self.state-1] == "R":
                self.swapLeft()
            self.state -= 1