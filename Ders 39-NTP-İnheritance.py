#Kalıtım
class calisan():
    def __init__(self,isim,maas,departman): # yapıcı fonksiyon
        print("Calışan sınıfının yapıcı fonksiyonu")
        self.isim=isim
        self.maas=maas
        self.departman=departman
    def bilgilerGoster(self):
        print("Calışan sınıfın bilgileri gösteriliyor")
        print("isim: ",self.isim,"maas: ",self.maas,"Departman: ",self.departman)
    def maasZam(self,zam):
        print("Maasa zam yapıldı")
        self.maas+=zam
    def departmanDegistir(self,yeniDepartman):
        print("Departman degistiriliyor.")
        self.departman=yeniDepartman

Calisan=calisan("Baran Güclü",2500,"Yazilim")
Calisan.bilgilerGoster()

class yonetici(calisan):
    def __init__(self,isim,maas,departman,kisiSayisi):
        #yapıcı fonksiyon girdisi (overriding
        print("yönetici sınıfının yapıcı fonksiyonu çagırılıyor...")
        """self.isim=isim
        self.maas=maas
        self.departman=departman"""
        super().__init__(isim, maas, departman)
        self.kisiSayisi=kisiSayisi
        super().bilgilerGoster()
    def bilgilerGoster(self): #overriding ettik.
        print("Yönetici sininin bilgileri gösteriliyor")



Yonetici =yonetici("Baran Güçlü",3000,"yazilim",20)




