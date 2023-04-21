#404 Kodlama Okulu 01.08.2022
# 404 Kodlama Okulu - Harun YÜKSEL

import play
import math

play.new_image(image="logo.png", size=100, transparency=5)
orta_top = play.new_circle(y =  100 , radius = 100)
yeni_top = play.new_circle(y = -250 , radius = 15)
skor = play.new_text(words = "0", y = 100 , font_size= 50 , color = "white")
sayi = 1
yazi = play.new_text(words = str(sayi) , y = -250, font_size= 25 , color = "white")
top = [yeni_top,yazi]
gonderilen_toplar = []
toplarin_acilari  = []
gonder = 0

@play.repeat_forever
async def repeat():
    global top
    global sayi
    if play.key_is_pressed("a"):
        while top[0].y < -20:
            for i in gonderilen_toplar:
                if top[0].is_touching(i[0]):
                    quit()
            await play.timer(1/1000)
            top[0].y += 15
            top[1].y = top[0].y
        else:
            sayi += 1
            gonderilen_toplar.append(top)
            top = [play.new_circle(y = -250 , radius = 15),play.new_text(words = str(sayi)
            ,y = -250, font_size= 25 , color = "white")]
            toplarin_acilari.append(270)
        await play.timer(seconds=0.1)


@play.repeat_forever
async def dondur():
    #Orta top etrafındaki topları sürekli ama sürekli döndürecek algoritmayı yazacağız.
    if len(gonderilen_toplar) != 0:
        for i in gonderilen_toplar:
            sira = gonderilen_toplar.index(i)
            i[0].x = 120*math.cos(toplarin_acilari[sira]*math.pi/180)
            i[0].y = 100 + 120*math.sin(toplarin_acilari[sira]*math.pi/180)
            i[1].x = 120 * math.cos(toplarin_acilari[sira] * math.pi / 180)
            i[1].y = 100 + 120 * math.sin(toplarin_acilari[sira] * math.pi / 180)
            toplarin_acilari[sira] +=4
        await play.timer(seconds=1/1000)
    skor.words = str(len(gonderilen_toplar))

play.start_program()