import random
import time

class kumanda():

    def __init__(self,tv_durumu = "KAPALI",tv_ses = 0,kanal_listesi = ["TRT1","ATV","STAR","SHOW TV","TV8"],kanal = "TRT1",ayarlar = ["Wi-fi","Bluetooth","Uydu Ayarları","Ekran Ayarı"],Wifi = "KAPALI",Bluetooth = "KAPALI",Uydu_ayarları = ["Türksat 3A","Türksat 4A","Türksat 5A"],Ekran_ayarları = ["Oyun","Sinema","Manzara","3D"]):
        self.tv_durumu = tv_durumu
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
        self.ayarlar = ayarlar
        self.Wifi = Wifi
        self.Bluetooth = Bluetooth
        self.Uydu_ayarları = Uydu_ayarları
        self.Ekran_ayarları = Ekran_ayarları

    def tv_ac(self):
        if self.tv_durumu == "AÇIK":
            print("TV zaten")
        else:
            print("TV açılıyor")
            time.sleep(2)
            self.tv_durumu = "AÇIK"
            print("Kanal:{} \nSes:{}".format(self.kanal,self.tv_ses))

    def tv_kapat(self):
        if self.tv_durumu == "KAPALI":
            print("TV zaten kapalı")
        else:
            print("TV kapanıyor")
            time.sleep(2)
            self.tv_durumu = "KAPALI"

    def ses_degistir(self):
        while True:
            ses = input("Sesi Azalt: '<'\nSesi Artır: '>'\n :")
            if ses == "<":
                if self.tv_ses != 0:
                    self.tv_ses -= 1
                    print("Ses Seviyesi {}".format(self.tv_ses))
            elif ses == ">":
                if self.tv_ses != 20:
                    self.tv_ses  += 1
                    print("Ses Seviyesi {}".format(self.tv_ses))
            else:
                print("Ses Seviyesi {}".format(self.tv_ses))
                break

    def kanal_ekle(self,kanal_ismi):
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi : {}".format(kanal_ismi))

    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]

    def menu(self):
        while True:
            print("Menü:\n",self.ayarlar)
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
            elif ayar == "Uydu Ayarları":
                Uydu_ayarları = input("Türksat 3A açmak için 1\nTürksat 4A açmak için 2\nTürksat 5A açmak için 3\nÇıkmak için q\n")
                if Uydu_ayarları == "1":
                    self.Uydu_ayarları = "Türksat 3A"
                    print("Uydu {}".format(self.Uydu_ayarları))
                elif Uydu_ayarları == "2":
                    self.Uydu_ayarları = "Türksat 4A"
                    print("Uydu {}".format(self.Uydu_ayarları))
                elif Uydu_ayarları == "3":
                    self.Uydu_ayarları = "Türksat 5A"
                    print("Uydu {}".format(self.Uydu_ayarları))
                else:
                    print("Menüden Çıkılıyor")
                    time.sleep(1)
                    break
            elif ayar == "Ekran Ayarı":
                Ekran_ayarları = input("Oyun Modu için 1\nSinema Modu için 2\nManzara Modu için 3\n3D Modu için 4\n :")
                if Ekran_ayarları == "1":
                    self.Ekran_ayarları = "Oyun Modu"
                    print("Ekran Modu {}".format(self.Ekran_ayarları))
                elif Ekran_ayarları == "2":
                    self.Ekran_ayarları = "Sinema Modu"
                    print("Ekran Modu {}".format(self.Ekran_ayarları))
                elif Ekran_ayarları == "3":
                    self.Ekran_ayarları = "Manzara Modu"
                    print("Ekran Modu {}".format(self.Ekran_ayarları))
                elif Ekran_ayarları == "4":
                    self.Ekran_ayarları = "3D"
                else:
                    print("Menüden Çıkılıyor")
                    time.sleep(1)
                    break
            else:
                print("Menüden çıkılıyor")
                time.sleep(1)
                break

    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "TV Durumu:{}\nTV Ses:{}\nKanal Listesi:{}\nŞu anda kanal:{}\nWi-fi {}\nBluetooth {}\nUydu {}\nEkran Modu {}".format(self.tv_durumu,self.tv_ses,self.kanal_listesi,self.kanal,self.Wifi,self.Bluetooth,self.Uydu_ayarları,self.Ekran_ayarları)

print("""
TV Uygulaması

1. Tv Aç
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısı
6. Rastgele Kanal
7. Televizyon Bilgileri
8. Ayar Menüsü

 Çıkmak için 'q' ya basın""")
Kumanda = kumanda()
while True:
    islem = input("İşlem Numarası: ")
    if islem == "q":
        print("Uygulamadan çıkılıyor...")
        time.sleep(1)
        break
    elif islem == "1":
        Kumanda.tv_ac()
    elif islem == "2":
        Kumanda.tv_kapat()
    elif islem == "3":
        Kumanda.ses_degistir()
    elif islem == "4":
        kanal_isimleri = input("Eklenecek kanalları ',' ile ayırarak giriniz:")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            Kumanda.kanal_ekle(eklenecekler)
    elif islem == "5":
        print("Kanal Sayısı :",len(Kumanda))
    elif islem == "6":
        Kumanda.rastgele_kanal()
        print("Kanal:",Kumanda.kanal)
    elif islem == "7":
        print(Kumanda)
    elif islem == "8":
        print(Kumanda.menu())
    else:
        print("Hatalı giriş...")
        time.sleep(1)

