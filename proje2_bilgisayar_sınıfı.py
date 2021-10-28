import time

class Pc():
    def __init__(self,pc_durumu = "KAPALI",pc_ses = 50,uygulama_listesi = ["Google Chrome","Bilgisayarım","Geri Dönüşüm Kutusu","Oyunlar"],acilacak_uyg = "Bilgisayarım",Ayarlar = ["Wi-fi","Bluetooth","Parlaklık","Ekran Ayarı"],Wifi = "KAPALI",Bluetooth = "KAPALI",Parlaklık = 50,Ekran_ayarı = ["Oyun","Sinema","Manzara"]):
        self.pc_durumu = pc_durumu
        self.pc_ses = pc_ses
        self.uygulama_listesi = uygulama_listesi
        self.Ayarlar = Ayarlar
        self.Wifi = Wifi
        self.Bluetooth = Bluetooth
        self.Parlaklık = Parlaklık
        self.Ekran_ayarı = Ekran_ayarı
        self.acilacak_uyg = acilacak_uyg

    def pc_ac(self):
        if self.pc_durumu == "KAPALI":
            print("PC açılıyor")
            time.sleep(1)
            self.pc_durumu = "AÇIK"
            print("Hoşgeldiniz")
        else:
            print("PC zaten açık")

    def pc_kapat(self):
        if self.pc_durumu == "AÇIK":
            print("PC kapanıyor")
            time.sleep(1)
            print("...")
            time.sleep(1)
            self.pc_durumu = "KAPALI"
            print("PC kapandı")
        else:
            print("PC zaten kapalı")

    def ses_degistir(self):
        while True:
            ses = input("Sesi Azalt: '<'\nSesi Artır: '>'\n :")
            if ses == "<":
                if self.pc_ses != 0:
                    self.pc_ses -= 1
                    print("Ses Seviyesi {}".format(self.pc_ses))
            elif ses == ">":
                if self.pc_ses != 20:
                    self.pc_ses  += 1
                    print("Ses Seviyesi {}".format(self.pc_ses))
            else:
                print("Ses Seviyesi {}".format(self.pc_ses))
                break
    def uygulama_indir(self,uyg_isimleri):
        time.sleep(1)
        self.uygulama_listesi.append(uyg_isimleri)
        print("Uygulama eklendi {}".format(uyg_isimleri))

    def uygulama_ac(self,acilacak_uyg):
        self.acilacak_uyg = acilacak_uyg
        print("{} başlatılıyor".format(self.acilacak_uyg))

    def __len__(self):
        return len(self.uygulama_listesi)
    def __str__(self):
        return "PC Durumu:{}\nPC Ses:{}\nUygulama Listesi:{}\nAçık uygulama :{}\nWi-fi {}\nBluetooth {}\nParlaklık {}\nEkran Modu {}".format(self.pc_durumu,self.pc_ses,self.uygulama_listesi,self.acilacak_uyg,self.Wifi,self.Bluetooth,self.Parlaklık,self.Ekran_ayarı)

    def menu(self):
        while True:
            print("Menü:\n",self.Ayarlar)
            ayar = input("Ayarlamak istediğiniz ayar adı giriniz:")
            if ayar == "Wi-fi":
                wifi = input("Wi-fi'yi açmak için 1\nWi-fi'yi kapatmak için 2\nÇıkmak için q\n")
                if wifi == "1":
                    self.Wifi = "AÇIK"
                    print("Wi-fi {}".format(self.Wifi))
                elif wifi == "2":
                    self.Wifi = "KAPALI"
                else:
                    print("Menüden Çıkılıyor")
                    time.sleep(1)
                    break

            elif ayar == "Bluetooth":
                bluetooth = input("Bluetooth'u açmak için 1\nBluetooth'u kapatmak için 2\nÇıkmak için q\n")
                if bluetooth == "1":
                    self.Bluetooth = "AÇIK"
                    print("Bluetooth {}".format(self.Bluetooth))
                elif bluetooth == "2":
                    self.Bluetooth = "KAPALI"
                    print("Bluetooth {}".format(self.Bluetooth))
                else:
                    print("Menüden Çıkılıyor")
                    time.sleep(1)
                    break
            elif ayar == "Parlaklık":
                while True:
                    Parlaklık = input("Parlaklık Azalt: '<'\nParlaklık Artır: '>'\n :")
                    if Parlaklık == "<":
                        if self.Parlaklık != 0:
                            self.Parlaklık -= 1
                            print("Parlaklık Seviyesi {}".format(self.Parlaklık))
                    elif Parlaklık == ">":
                        if self.Parlaklık != 20:
                            self.Parlaklık += 1
                            print("Parlaklık Seviyesi {}".format(self.Parlaklık))
                    else:
                        print("Parlaklık Seviyesi {}".format(self.Parlaklık))
                        break
            elif ayar == "Ekran Ayarı":
                Ekran_ayarları = input("Oyun Modu için 1\nSinema Modu için 2\nManzara Modu için 3\n3D Modu için 4\n :")
                if Ekran_ayarları == "1":
                    self.Ekran_ayarları = "Oyun Modu"
                    print("Ekran : {} etkin".format(self.Ekran_ayarları))
                elif Ekran_ayarları == "2":
                    self.Ekran_ayarları = "Sinema Modu"
                    print("Ekran : {} etkin".format(self.Ekran_ayarları))
                elif Ekran_ayarları == "3":
                    self.Ekran_ayarları = "Manzara Modu"
                    print("Ekran : {} etkin".format(self.Ekran_ayarları))
                elif Ekran_ayarları == "4":
                    self.Ekran_ayarları = "3D"
                    print("Ekran : {} etkin".format(self.Ekran_ayarları))
                else:
                    print("Menüden Çıkılıyor")
                    time.sleep(1)
                    break
            else:
                print("Menüden çıkılıyor")
                time.sleep(1)
                break


print("""
PC Uygulaması

1. Pc Aç
2. Pc Kapat
3. Ses Ayarları
4. Uygulama İndir
5. Çalışan uygulama sayısı
6. Uygulama çalıştır
7. Pc Bilgileri
8. Ayar Menüsü

 Çıkmak için 'q' ya basın""")
pc1 = Pc()
while True:
    islem = input("İşlem Numarası: ")
    if islem == "q":
        print("Uygulamadan çıkılıyor...")
        time.sleep(1)
        break
    elif islem == "1":
        pc1.pc_ac()
    elif islem == "2":
        pc1.pc_kapat()
    elif islem == "3":
        pc1.ses_degistir()
    elif islem == "4":
        uyg_isimleri = input("İndirilecek Uygulamaları ',' ile ayırarak giriniz:")
        uygulama_listesi = uyg_isimleri.split(",")
        for indirilecekler in uygulama_listesi:
            pc1.uygulama_indir(indirilecekler)
    elif islem == "5":
        print("Uygulama Sayısı :",len(pc1))
    elif islem == "6":
        acilacak_uyg = input("Açılacak uygulamanın ismini giriniz:")
        print(pc1.uygulama_ac(acilacak_uyg))
    elif islem == "7":
        print(pc1)
    elif islem == "8":
        print(pc1.menu())
    else:
        print("Hatalı giriş...")
        time.sleep(1)
