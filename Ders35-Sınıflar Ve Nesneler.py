#Sınıflar Ve Nesneler
class dusman:
    kalanCan= 3
    def saldir(self):
        print("Hücum")
        self.kalanCan -=1
    def hayattaMi(self):
        if(self.kalanCan<=0):
            print("Öldü")
        else:
            print(str(self.kalanCan)+"cani kaldi")
dusman1=dusman()
dusman2=dusman()
dusman1.saldir()
dusman1.saldir()
dusman1.hayattaMi()

