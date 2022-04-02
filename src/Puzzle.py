from Ubin import Ubin

# Kelas untuk menyimpan puzzle
class Puzzle:
    # Mencari index dari ubin dengan nilai yang diinginkan
    def findUbinLocation(self, value):
        for i in range(16):
            if self.ubin[i].value == value:
                return i
        return -1

    # Mencari nilai dari KURANG(i)
    def kurang(self, i):
        count = 0
        idx = self.findUbinLocation(i+1)
        for j in range(idx, 16):
            if self.ubin[idx].value > self.ubin[j].value:
                count += 1
        return count

    # Mencari jumlah dari seluruh KURANG(i)
    def findSumOfKurang(self):
        sum = 0
        for i in range(16):
            kurang_i = self.kurang(i)
            print(f"KURANG({i+1}) = {kurang_i}")
            sum += kurang_i
        return sum

    # Mengembalikan setiap dilai dari KURANG(i) dalam bentuk list
    def getKurangList(self):
        kurangList = []
        self.sumOfKurang = 0
        for i in range(16):
            kurang_i = self.kurang(i)
            kurangList.append(kurang_i)
            self.sumOfKurang += kurang_i
        return kurangList

    # Mengecek nilai dari X sesuai lokasi ubin kosong
    def checkX(self):
        if self.blankUbin == 0:
            self.X = 0
        if self.blankUbin == 1:
            self.X = 1
        if self.blankUbin == 2:
            self.X = 0
        if self.blankUbin == 3:
            self.X = 1
        if self.blankUbin == 4:
            self.X = 1
        if self.blankUbin == 5:
            self.X = 0
        if self.blankUbin == 6:
            self.X = 1
        if self.blankUbin == 7:
            self.X = 0
        if self.blankUbin == 8:
            self.X = 0
        if self.blankUbin == 9:
            self.X = 1
        if self.blankUbin == 10:
            self.X = 0
        if self.blankUbin == 11:
            self.X = 1
        if self.blankUbin == 12:
            self.X = 1
        if self.blankUbin == 13:
            self.X = 0
        if self.blankUbin == 14:
            self.X = 1
        if self.blankUbin == 15:
            self.X = 0
        return self.X

    # ctor
    def __init__(self, listUbin):
        self.ubin = [Ubin(i) for i in listUbin]     # Isi dari Ubin
        self.steps = []         # Langkah yang dilakukan
        self.stepsCount = 0     # Jumlah langkah yang dilakukan

        # Mencari lokasi ubin kosong
        for i in range(16):
            if listUbin[i] == 16 :
                self.blankUbin = i
                break


        
    # Menginisialisasi CLI
    def initializeCLI(self):
        print("Posisi awal:")
        self.print()
        
        self.sumOfKurang = self.findSumOfKurang()
        self.checkX()
        print(f"X = {self.X}")

        print(f"Sum of KURANG(i) + X = {self.sumOfKurang + self.X}")
        print()


    # Mendapatkan langkah terakhir yang dilakukan
    def getLastStep(self):
        return self.steps[-1] if len(self.steps) > 0 else "No steps"



    # Menukar 2 ubin
    def swap(self, i, j):
        temp = self.ubin[i]
        self.ubin[i] = self.ubin[j]
        self.ubin[j] = temp

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

    # Menghitung ubin yang tidak berada pada tempat seharusnya
    def countNotInRightPlace(self):
        count = 0
        for i in range(16):
            if self.ubin[i].value != i+1:
                count += 1
        return count

    # Menggeser ubin kosong ke atas
    def swapUp(self):
        topUbin = self.blankUbin - 4
        self.swap(topUbin, self.blankUbin)
        self.blankUbin = topUbin
        self.steps.append("U")
        self.stepsCount += 1
        #print("U")
        #self.print()

    # Menggeser ubin kosong ke bawah
    def swapDown(self):
        bottomUbin = self.blankUbin + 4
        self.swap(bottomUbin, self.blankUbin)
        self.blankUbin = bottomUbin
        self.steps.append("D")
        self.stepsCount += 1
        #print("D")
        #self.print()
    
    # Menggeser ubin kosong ke kiri
    def swapLeft(self):
        leftUbin = self.blankUbin - 1
        self.swap(leftUbin, self.blankUbin)
        self.blankUbin = leftUbin
        self.steps.append("L")
        self.stepsCount += 1
        #print("L")
        #self.print()
    
    # Menggeser ubin kosong ke kanan
    def swapRight(self):
        rightUbin = self.blankUbin + 1
        self.swap(rightUbin, self.blankUbin)
        self.blankUbin = rightUbin
        self.steps.append("R")
        self.stepsCount += 1
        #print("R")
        #self.print()

    # Mengembalikan isi dari puzzle dalam bentuk list of string
    def toStringList(self):
        list = []
        for i in range(16):
            list.append(str(self.ubin[i].value if self.ubin[i].value != 16 else " ").rjust(2, ' '))
        print(list)
        return list

    def toUbinId(self):
        id = ""
        for i in range(16):
            id += str(self.ubin[i].value)
        return id