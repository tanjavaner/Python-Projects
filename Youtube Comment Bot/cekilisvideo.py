import random
from time import sleep

import pyautogui as pg
import pyperclip
from pyautogui import Point

# yorumlar = list()
# with open("yorumlar.txt", "r+", encoding="utf-8") as file:
#    for i in file:
#        yorumlar.append(i.rstrip("\n"))

yorum = input("Yorumu yaz.")
link = input("Linki yaz.")

hesaplar = [Point(x=237, y=283), Point(x=445, y=299), Point(x=617, y=291), Point(x=800, y=294), Point(x=974, y=290),
            Point(x=1139, y=294), Point(x=1316, y=289), Point(x=1499, y=289), Point(x=1676, y=292), Point(x=253, y=482),
            Point(x=420, y=487), Point(x=611, y=487), Point(x=779, y=480), Point(x=969, y=486), Point(x=1132, y=489),
            Point(x=1314, y=486), Point(x=1491, y=485), Point(x=1676, y=485), Point(x=244, y=688), Point(x=421, y=674),
            Point(x=588, y=672), Point(x=800, y=679), Point(x=983, y=671), Point(x=1129, y=673), Point(x=1343, y=679),
            Point(x=1492, y=686), Point(x=1659, y=682), Point(x=241, y=866)]

random.shuffle(hesaplar)
turuncuoyuncu = [Point(x=719, y=249), Point(x=722, y=303), Point(x=728, y=357), Point(x=717, y=405),
                 Point(x=961, y=208), Point(x=961, y=251), Point(x=961, y=307), Point(x=957, y=357),
                 Point(x=1206, y=203), Point(x=1203, y=254), Point(x=1199, y=300), Point(x=1195, y=355)]
sifir = [Point(x=713, y=245), Point(x=711, y=306), Point(x=718, y=364), Point(x=719, y=400), Point(x=955, y=199),
         Point(x=953, y=256), Point(x=954, y=302), Point(x=948, y=353), Point(x=948, y=410), Point(x=1191, y=205),
         Point(x=1194, y=252), Point(x=1191, y=307), Point(x=1190, y=355)]
mehmetaykin = [Point(x=732, y=247), Point(x=736, y=306), Point(x=724, y=364), Point(x=970, y=193), Point(x=973, y=256),
               Point(x=969, y=300), Point(x=1193, y=205), Point(x=1193, y=245), Point(x=1199, y=302)]
multiple = [Point(x=611, y=487), Point(x=779, y=480), Point(x=1491, y=485)]  # Turuncu Oyuncu , Sıfır
switcher = "https://www.youtube.com/channel_switcher"


def fonksiyon(switcher_link, video_link, comment, switcher_coordinate=None):
    if switcher_coordinate != None:
        pg.click(Point(x=255, y=48))
        pg.write(switcher_link)
        pg.press("enter")
        sleep(2.5)
        pg.click(switcher_coordinate)
        sleep(1.5)
    pg.click(Point(x=255, y=48))
    pg.write(video_link)
    sleep(4)
    pg.press("space")
    sleep(1)
    pg.moveTo(x=1912, y=110)
    pg.dragTo(x=1912, y=268, duration=2, button="left")
    try:
        t = pg.locateCenterOnScreen("yorumalt80.png")
        pg.click(t[0], t[1] - 10)
        sleep(0.5)
        pyperclip.copy(comment)
        pg.hotkey('ctrl', 'v')
        sleep(2)
        pg.click(pg.locateCenterOnScreen("yorumyap80.png", grayscale=False))
    except:
        t = pg.locateCenterOnScreen("yorumalt100.png")
        pg.click(t[0], t[1] - 10)
        sleep(1)
        pyperclip.copy(comment)
        pg.hotkey('ctrl', 'v')
        sleep(2)
        pg.click(pg.locateCenterOnScreen("yorumyap100.png", grayscale=False))
    sleep(5)


print("2 saniyeye başlıyoruz . Mouse'u sabit bırak. ")
sleep(2)

for i in hesaplar:
    sleep(0.5)
    pg.click(753, 1058)
    sleep(0.5)
    pg.click(1403, 136)
    sleep(0.6)
    pg.click(i)
    sleep(0.5)
    if i in multiple:
        if i == Point(x=611, y=487):  # TuruncuOyuncu
            for t in turuncuoyuncu:
                fonksiyon(switcher, link, yorum, t)
            pg.click(1896, 15)
            sleep(1)
        elif i == Point(x=779, y=480): # Sıfır
            for t in sifir:
                fonksiyon(switcher, link, yorum, t)
            pg.click(1896, 15)
            sleep(1)
        else:
            for t in mehmetaykin: # Mehmet Aykın
                fonksiyon(switcher, link, yorum, t)
            sleep(1)
            pg.click(1896, 15)
    else:
        fonksiyon(switcher, link, yorum)
        sleep(1)
        pg.click(1896, 15)
