# Harun YÜKSEL
import random
import os
import time


OKGREEN = '\033[92m'
ENDC = '\033[0m'
devam = "R"

while devam != "Q":
    os.system('cls')
    yanlis_hakki = 2
    dogru_sayisi = 0
    yanlis_sayisi = 0
    ders = input("Hangi derse çalışmak istiyorsun ? (1,2,3,4,5,6,7,Hepsini kombine etmek için 8) :")
    if ders != "8":
        with open("lecture"+ders+".txt", "r+", encoding="utf-8") as f:
            sozcukler = f.readlines()
            kelimeler = list()
            for i in range(len(sozcukler)):
                sozcukler[i] = sozcukler[i].rstrip('\n')
                kelimeler.append(sozcukler[i].split("*")[1])
                sozcukler[i] = sozcukler[i].split("*")[0] + "----------" + sozcukler[i].split("*")[2]
    else:
        sozcukler = []
        kelimeler = []
        for i in range(1,8):
            with open("lecture"+str(i)+".txt", "r+", encoding="utf-8") as f:
                sozcuklerr = f.readlines()
                kelimelerr = list()
                for i in range(len(sozcuklerr)):
                    sozcuklerr[i] = sozcuklerr[i].rstrip('\n')
                    kelimelerr.append(sozcuklerr[i].split("*")[1])
                    sozcuklerr[i] = sozcuklerr[i].split("*")[0] + "----------" + sozcuklerr[i].split("*")[2]
                for i in sozcuklerr:
                    sozcukler.append(i)
                for t in kelimelerr:
                    kelimeler.append(t)
    
    kalansoru = len(sozcukler)
    while kalansoru:
        os.system('cls')
        sozcuk = random.randint(0, len(sozcukler) - 1)
        a = kelimeler[sozcuk]
        b = random.choice(kelimeler)
        c = random.choice(kelimeler)
        d = random.choice(kelimeler)
        e = random.choice(kelimeler)
        f = random.choice(kelimeler)
        g = random.choice(kelimeler)
        tamam = False
        while not tamam:
        
            if sozcukler[sozcuk].endswith("soruldu") or f.lower() == a.lower or a.lower() == b.lower() or a.lower() == c.lower() or a.lower() == d.lower() or a.lower() == e.lower() or b.lower() == c.lower() or b.lower() == d.lower() or b.lower() == e.lower() or c.lower() == d.lower() or c.lower() == e.lower() or d.lower() == e.lower() or f.lower() == b.lower() or f.lower() == c.lower() or f.lower() == d.lower() or f.lower() == e.lower() or f.lower() == g.lower() or g.lower() == a.lower() or g.lower() == b.lower() or g.lower() == c.lower() or g.lower() == d.lower() or g.lower() == e.lower():
                sozcuk = random.randint(0, len(sozcukler) - 1)
                a = kelimeler[sozcuk]
                b = random.choice(kelimeler)
                c = random.choice(kelimeler)
                d = random.choice(kelimeler)
                e = random.choice(kelimeler)
                f = random.choice(kelimeler)
                g = random.choice(kelimeler)
            else:
                tamam = True
        siklar = [a, b, c, d, e, f, g]
        random.shuffle(siklar)
        print("Ders {} \nKalan Soru : {} \nDoğru : {}\nYanlış : {}\n".format(ders,kalansoru,dogru_sayisi,yanlis_sayisi))
        print(OKGREEN + f"{sozcukler[sozcuk]}"+ENDC)
        print("""
    1: {} , 2: {} , 3: {} , 4: {}, 5: {}, 6: {}, 7: {}
        """.format(siklar[0], siklar[1], siklar[2], siklar[3], siklar[4],siklar[5],siklar[6]))
        cevap = int(input("Cevabınız : "))
        #kelimeler.index(siklar[cevap - 1]) == sozcuk:
        #siklar[cevap - 1] == kelimeler[sozcukler.index(sozcuk)]
        if siklar[cevap - 1] == kelimeler[sozcuk]:
            print("Doğru cevap.")
            dogru_sayisi += 1
            sozcukler[sozcuk] += "soruldu"
            kalansoru -=1
            time.sleep(0.3)
        else:
            print("Yanlış.")
            yanlis_sayisi += 1
            
            print("""
            
            Doğru cevap : {}
            
            """.format(kelimeler[sozcuk]))
            input("Devam etmek için herhangi bir tuşa bas...")
        os.system('cls')
    else:
        print("Tüm soruları bitirdin")
        devam = input("Programdan çıkmak için 'Q' yazınız")
    