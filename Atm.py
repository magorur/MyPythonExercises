import time

sifre = "sifreparola"
bakiye = 2885
while True:
    print("""
    ***Banka ATM Cihazı***
    Lütfen yapmak istediğiniz işlemi seçiniz
    1 Para çekme 
    2 Para yatırma
    3 Kredi kartı işlemleri
    4 Ödeme işlemleri
    5 Şifre işlemleri
    6 Döviz işlemleri
    7 Bakiye sorgulama
    8 Çıkış

    """)
    islem = int(input("İşlem Numarası: "))
    if islem == 8:
        print("Çıkış yapıldı.")
        print("iyi günler...")
        break
    elif islem == 1:
        print("""
        ---Para çekme---
        Lütfen çekmek istediğiniz tutarı giriniz. 
        (max çekilebilecek tutar {} tl""".format(bakiye))
        cekilen = int(input(":"))
        if cekilen <= 0:
            print("hatalı giriş")
            print("Ana Menüye geçildi")
            time.sleep(1)
            continue
        elif cekilen > bakiye:
            print("Hesabınızdakinden fazla para çekimi yapamazsınız")
            print("Ana Menüye geçildi")
            time.sleep(1)
            continue
        else:
            bakiye -=cekilen
            print("Kalan bakiyeniz {} tl".format(bakiye))
            print("Ana Menüye geçildi")
            time.sleep(1)
    elif islem == 2:
        print("""
                ---Para yatırma---
                Lütfen yatırmak istediğiniz tutarı giriniz.""")
        yatirilan = int(input(":"))
        if yatirilan <= 0:
            print("hatalı giriş")
            print("Ana Menüye geçildi")
            time.sleep(1)
            continue
        elif yatirilan > 10000:
            print("bu miktardaki parayı lütfen vezneden yatırınız ")
            print("Ana Menüye geçildi")
            time.sleep(1)
            continue
        else:
            bakiye += yatirilan
            print("Yeni bakiye {} tl".format(bakiye))
            print("Ana Menüye geçildi")
            time.sleep(1)
    elif islem == 3:
        print("""
        Kart işlemleri
        1 Kart ekstresi
        2 Kart ödemesi
        3 Kart limiti ayarlama
        4 Ana menü
        """)
        k_islem = int(input("art işlemi numarası: "))
        if k_islem == 4:
            print("Ana menüye dönüldü.")
            time.sleep(1)
            continue
        elif k_islem == 1:
            print("Kart ekstreleri:")
            print("""
            \n1.ay\n2.ay\n3.ay\n4.ay\n5.ay\n6.ay\n7.ay\n8.ay\n9.ay\n10.ay\n11.ay\n12.ay
            """)
            print("Ana Menüye geçildi")
            time.sleep(1)
        elif k_islem == 2:
            print("Kart ödemesi")
            odeme = int(input("Ödenecek miktar:"))
            print("{} tl kart ödemesi yapıldı".format(odeme))
            print("Ana Menüye geçildi")
            time.sleep(1)
        elif k_islem == 3:
            limit = 2000
            print("Kart limiti ayarı")
            print("Şu an limitiniz:{} tl".format(limit))
            limit = int(input("Yeni limit:"))
            if limit <= 0 and limit > 6000:
                print("böyle bir limit girişi ayarlanamaz")
                limit = 2000
                print("Ana Menüye geçildi")
                time.sleep(1)
                continue
            else:
                print("Yeni limitiniz {} tl olarak ayarlandı".format(limit))
                print("Ana Menüye geçildi")
                time.sleep(1)
    elif islem == 4:
        print("Ödeme işlemleri")
        print("""
        1 Kira Ödeme
        2 Harç Ödeme
        3 Fatura Ödeme
        4 Tapu Ödeme
        5 Vergi Ödeme
        6 SGK Ödeme
        7 Ana Menü
        """)
        odeme_islemi = int(input("Ödeme işlem numarası: "))
        if odeme_islemi == 1:
            kira_miktari = int(input("Kira ödenecek miktar:"))
            print("Kira ödenecek hesap no: ")
            hesap_no = int(input("TR"))
            print("Girdiğiniz hesap no TR{} ve kira miktarı {} tl".format(hesap_no,kira_miktari))
            print("Ana Menüye geçildi")
            time.sleep(1)
        elif odeme_islemi == 2:
            kira_miktari = int(input("Harç ödenecek miktar:"))
            print("Harç ödenecek hesap no: ")
            hesap_no = int(input("TR"))
            print("Girdiğiniz hesap no TR{} ve harç miktarı {} tl".format(hesap_no, kira_miktari))
            print("Ana Menüye geçildi")
            time.sleep(1)
        elif odeme_islemi == 3:
            kira_miktari = int(input("Fatura ödenecek miktar:"))
            print("Fatura ödenecek hesap no: ")
            hesap_no = int(input("TR"))
            print("Girdiğiniz hesap no TR{} ve fatura miktarı {} tl".format(hesap_no, kira_miktari))
            print("Ana Menüye geçildi")
            time.sleep(1)
        elif odeme_islemi == 4:
            kira_miktari = int(input("Tapu ödenecek miktar:"))
            print("Tapu ödenecek hesap no: ")
            hesap_no = int(input("TR"))
            print("Girdiğiniz hesap no TR{} ve tapu miktarı {} tl".format(hesap_no, kira_miktari))
            print("Ana Menüye geçildi")
            time.sleep(1)
        elif odeme_islemi == 5:
            kira_miktari = int(input("Vergi ödenecek miktar:"))
            print("Vergi ödenecek hesap no: ")
            hesap_no = int(input("TR"))
            print("Girdiğiniz hesap no TR{} ve Vergi miktarı {} tl".format(hesap_no, kira_miktari))
            print("Ana Menüye geçildi")
            time.sleep(1)
        elif odeme_islemi == 6:
            kira_miktari = int(input("SGK ödenecek miktar:"))
            print("SGK ödenecek hesap no: ")
            hesap_no = int(input("TR"))
            print("Girdiğiniz hesap no TR{} ve SGK miktarı {} tl".format(hesap_no, kira_miktari))
            print("Ana Menüye geçildi")
            time.sleep(1)
        elif odeme_islemi == 7:
            print("Ana Menüye geçildi.")
            time.sleep(1)
            continue
    elif islem == 5:
        print("""
        Şifre işlemleri
        1 Şifre değiştirme
        2 Ana Menü
        """)
        s_islemi = int(input("Şifre işlem numarası: "))
        if s_islemi == 1:
            yenisifre = input("Yeni Şifrenizi giriniz:")
            if yenisifre == sifre:
                print("Yeni şifreniz eskisi ile aynı olamaz")
                time.sleep(1)
            else:
                yenisifre = sifre
                print("Şifre başarıyla değiştirildi")
                time.sleep(1)
                continue
        elif s_islemi == 2:
            print("Ana Menüye geçildi.")
            time.sleep(1)
        else:
            print("Hatalı şifre işlem numarası")
            time.sleep(1)
            continue
    elif islem == 6:
        print("""Döviz işlemleri
        1 Altın
        2 Dolar
        3 Euro
        4 Diğer
        5 Ana Menü
        """)
        doviz_islem = int(input("Döviz işlem numarası:"))
        if doviz_islem == 5:
            print("Ana Menüye geçildi.")
            time.sleep(1)
            continue
        elif doviz_islem == 1:
            print("Altın hesabı")
        elif doviz_islem == 2:
            print("Dolar hesabı")
        elif doviz_islem == 3:
            print("Euro hesabı")
        elif doviz_islem == 4:
            print("Lütfen işlem yapmak istediğiniz dövizi seçiniz")
        else:
            print("hatalı döviz işlem numarası")
            time.sleep(1)
            continue
    elif islem == 7:
        print("Bakiye sorgulama ekranı")
        print("Mevcut bakiyeniz {} tl".format(bakiye))
        time.sleep(1)
    else:
        print("hatalı işlem numarası...")
        time.sleep(1)
        continue