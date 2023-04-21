import play
import pygame
import os
import random
#Dosya işlemleri için uygun kütüphane

play.set_backdrop("light blue")
play.new_image(image="logo.png", size=120, transparency=10)
muzikdegistir = play.new_circle(radius=60, color="red", x=-200, border_width=2, border_color="black")
muzikduraklat = play.new_circle(radius=60, color="red", x=0, border_width=2, border_color="black")
muzikbilgi = play.new_text(words="Henüz bir şey çalmıyor.", x=0, y=100, font_size=40)
kapat = play.new_box(width=40, height=40, color="red", x=(play.screen.width/2)-20, y=play.screen.height/2-20)
bastanbaslat = play.new_circle(radius=60, color="red", x=200, border_width=2, border_color="black")
karisik = play.new_circle(radius=60, color="red", x=0, y=-200, border_width=2, border_color="black")

yazi_1 = play.new_text(words="Sonraki müzik", x=-200, font_size=25)
yazi_2 = play.new_text(words="=", x=0, font_size=25)
yazi_3 = play.new_text(words="Baştan başla", x=200, font_size=25)
yazi_4 = play.new_text(words="X", x=(play.screen.width/2)-20, y=play.screen.height/2-20, font_size=50)
yazi_5 = play.new_text(words="Karışık çal", y=-200, font_size=25)




muziklistesi = []
for i in os.listdir():
    if i[-3:] == "mp3":
        muziklistesi.append(i)

guncel = 0


@muzikdegistir.when_clicked
async def degistir():
    global guncel
    #Değişken global alanda olduğu için global olarak tanımladık.
    if guncel == len(muziklistesi)-1:
        guncel = 0
    else:
        guncel += 1
    pygame.mixer.music.load(muziklistesi[guncel])
    pygame.mixer.music.play()
    muzikbilgi.words = "Şuan " + muziklistesi[guncel][:-4] + " çalınıyor."
    await play.timer(seconds=0.1)


tiklandi = 0


@muzikduraklat.when_clicked
async def duraklat():
    global tiklandi
    if tiklandi == 0:
        pygame.mixer.music.pause()
        muzikbilgi.words = muziklistesi[guncel][:-4] + " duraklatıldı."
        muzikduraklat.color = "blue"
        tiklandi = 1
    else:
        pygame.mixer.music.unpause()
        tiklandi = 0
        muzikbilgi.words = "Şuan " + muziklistesi[guncel][:-4] + " çalınıyor."
        muzikduraklat.color = "red"
    await play.timer(seconds=0.1)


@bastanbaslat.when_clicked
async def bastan():
    pygame.mixer.music.load(muziklistesi[guncel])
    pygame.mixer.music.play()
    await play.timer(seconds=0.1)


@karisik.when_clicked
async def karistir():
    global guncel
    guncel = random.randint(0, len(muziklistesi)-1)
    pygame.mixer.music.load(muziklistesi[guncel])
    pygame.mixer.music.play()
    muzikbilgi.words = "Şuan " + muziklistesi[guncel][:-4] + " çalınıyor."
    await play.timer(seconds=0.1)


@kapat.when_clicked
def kapat():
    quit()

play.start_program()