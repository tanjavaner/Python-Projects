import play
import random


arkaplan = play.new_image(image = "arkaplan.png",size = 130)
kus = play.new_image(image ="kus.png",x=-100,size=9)
engel_1 = play.new_box(x = 440,y = 300 ,height = 350,width =80,color = "blue",border_width= 5,border_color="black")
engel_2 = play.new_box(x = 440,y = -300,height = 550,width =80,color = "blue",border_width= 5,border_color="black")
kus.start_physics(stable = True , can_move= True , obeys_gravity= True,bounciness = 0.5)
puan = 0
skor = play.new_text(words = str(puan),x = 350,y = 250)
@play.repeat_forever
def zipla():
    global puan
    skor.words = str(puan)
    if play.key_is_pressed("w","W"):
        kus.physics.y_speed = 30
    if engel_1.x > -450:
        engel_1.x -= 5
        engel_2.x -= 5
    else :
        engel_1.x = 440
        engel_2.x = 440
        rastgelesayi = random.randint(0,940)
        engel_1.height = 940-rastgelesayi
        engel_2.height = rastgelesayi
    if engel_1.x == -100:
        puan += 1
    if kus.is_touching(engel_1) or kus.is_touching(engel_2):
        puan = 0
        engel_1.x = 440
        engel_2.x = 440
play.start_program()

