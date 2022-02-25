#İnit Fonksiyonu
class dusman:
    def __init__(self,isim,kalanCan,saldiriGucu,mermiSayisi):
        self.isim = isim
        self.kalanCan = kalanCan
        self.saldiriGucu = saldiriGucu
        self.mermiSayisi = mermiSayisi
    def print(self):
        print("Basılıyor.....")
        print("isim: ",self.isim,"Kalan can: ",self.kalanCan,"Saldiri gücü: ",self.saldiriGucu,"Mermi Sayisi: ",self.mermiSayisi)
dusman1 =dusman("Ali",2000,30,50)
dusman2=dusman("Baran",1000,20,40)
print("Dusman1----------")
dusman1.print()
print("Dusman2-----------")
dusman2.print()
