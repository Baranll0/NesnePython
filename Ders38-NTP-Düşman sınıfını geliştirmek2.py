import random
class dusman:
    def __init__(self,isim="Dusman",kalan_can=500,saldiri_gücü=10,mermi_sayisi=5):
        self.isim=isim
        self.kalan_can=kalan_can
        self.saldiri_gücü=saldiri_gücü
        self.mermi_sayisi=mermi_sayisi

    def saldir(self):
        print(self.isim+"saldiriyor")
        harcanan_mermi=random.randrange(0,10)
        print(str(harcanan_mermi)+"kadar mermi harcandı")
        self.mermi_sayisi=harcanan_mermi
        return (harcanan_mermi,self.saldiri_gücü)
    def savunma(self,harcanan_mermi,saldiri_gücü):
        print(self.isim+"Vuruldum.....")
        self.kalan_can-=(harcanan_mermi*saldiri_gücü)
    def mermiKontrol(self):
        if(self.mermi_sayisi<=0):
            print(self.isim +"Konuşuyor... Mermim bitti destek lazım")
        return True
    def hayattaMi(self):
        if(self.kalan_can<=0):
            print(self.isim+"konuşuyor... Ölüyorumm")


    def print(self):
        print("Basılıyor......")
        print("isim",self.isim,"Kalan can: ",self.kalan_can,"Saldiri Gücü: ",self.saldiri_gücü,"Mermi Sayisi: ",self.mermi_sayisi)

dusmanlar=[]
i=0
while (i<10):
    rastgele_can=random.randrange(100,200)
    rastgele_saldirigücü=random.randrange(10,20)
    rastgele_mermi=random.randrange(20,30)
    yenidusman=dusman("Dusman"+str(i+1),rastgele_can,rastgele_saldirigücü,rastgele_mermi)
    dusmanlar.append(yenidusman)
    i +=1
i=0
while(i<3):
    randomdusman1=random.randrange(0,10)
    randomdusman2=random.randrange(0,10)
    donendeger=dusmanlar[randomdusman1].saldir()
    dusmanlar[randomdusman2].savunma(donendeger[0],donendeger[1])
    print("Raunt Bitti....")
    i += 1

