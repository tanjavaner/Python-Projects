import play
from random import *

play.set_backdrop("light blue")
ozelarkaplan = play.new_image(image = "ozelarkaplan.jpg",size = 800 , y = -250)
platform = play.new_box(width = 100 , height = 50 , y = -250,color = (30,218,30)
,border_color= "black",border_width=5)
ozelarkaplan.hide()
skorlama = play.new_text(words = "0" , x = 350 , y = 250)
skor = 0

yumurtalar = []

@play.repeat_forever
def platformhareket():
    if play.key_is_pressed("a","A"):
        platform.x -= 6
    if play.key_is_pressed("d","D"):
        platform.x += 6

@play.repeat_forever  # Yumurtaları rastgele x koordinatlarıyla beraber oluşturacak.
async def yumurtaspawn():
    yumurta = play.new_circle(color = "white" , border_color= "black"
    ,border_width=3 , radius = 15 , x = randint(-380,380), y = 350)
    yumurtalar.append(yumurta)
    await play.timer(seconds = 1.5)

@play.repeat_forever
def yumurtadusur():
    global skor
    for i in yumurtalar:
        i.y -= 5
        if i.is_touching(platform):
            skor += 1
            skorlama.words = str(skor)
            i.hide()
            yumurtalar.remove(i)
        if i.y < -300 :
            quit()


@play.repeat_forever
async def ozelyetenek():
    if play.key_is_pressed("r","R"):
        ozelarkaplan.show()
        for i in yumurtalar:
            i.color = "yellow"
        await play.timer(seconds = 0.1)

        for i in yumurtalar:
            i.color = "orange"
        await play.timer(seconds = 0.1)

        for i in yumurtalar:
            i.color = "red"
        await play.timer(seconds = 0.1)

        for i in yumurtalar:
            i.hide()
            yumurtalar.remove(i)
        ozelarkaplan.hide()




play.start_program()
