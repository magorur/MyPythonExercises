class Hayvanlar():
    def __init__(self,hücre_duvarı = "YOK",hücre_tipi = "çok hücreli",hücre_yapısı = "ökaryot",dokular = ["sinir dokuları","bağ dokuları","kas dokuları","epitel dokuları"],üreme = "Eşeyli üreme",beslenme_türü = "heterotrof"):
        self.hücre_duvarı = hücre_duvarı
        self.hücre_tipi = hücre_tipi
        self.hücre_yapısı = hücre_yapısı
        self.dokular = dokular
        self.üreme = üreme
        self.beslenme_türü = beslenme_türü

class Köpekler(Hayvanlar):
    def __init__(self,koku = "gelişmiş",işitme = "güçlü",beslenme = "etçil"):
        print("Köpek")
        self.koku = koku
        self.işitme = işitme
        self.beslenme = beslenme

    def ozellikler(self):
        print("Koku alma {} İşitme {} Beslenme tipi {}".format(self.koku,self.işitme,self.beslenme))


class Kuşlar(Hayvanlar):
    def __init__(self,kanat = "var",uçabilme = "var",sevdiği_iklim = "sıcak"):
        print("Kuş")
        self.kanat = kanat
        self.uçabilme = uçabilme
        self.sevdiği_iklim = sevdiği_iklim

    def ozellikler(self):
        print("Kanatları {} Uçabilme yeteneği {} {} iklim sever".format(self.kanat,self.uçabilme,self.sevdiği_iklim))


class Atlar(Hayvanlar):
    def __init__(self,işitme = "güçlü",yele = "var",beslenme = "otçul",kuyruk = "var"):
        print("At")
        self.işitme = işitme
        self.yele = yele
        self.beslenme = beslenme
        self.kuyruk = kuyruk

    def ozellikler(self):
        print("Yelesi {} İşitme yeteneği {} Kuyruğu {} Beslenme türü {}".format(self.yele,self.işitme,self.kuyruk,self.beslenme))

at = Atlar()
print(at.ozellikler())

kuş = Kuşlar()
print(kuş.ozellikler())

köpek = Köpekler()
print(köpek.ozellikler())