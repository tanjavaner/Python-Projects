durum = int(input("Bir yüze kaç sayfa yazdırılacak (1,2,4) :"))
sayfa = int(input("Sayfa sayısını gir :"))
on_sayfa = list()
arka_sayfa = list()
tek = 0
t = 1

while t <= sayfa:
    if tek % 2 == 0:
        on_sayfa.append(t)
    else:
        arka_sayfa.append(t)

    if t % durum == 0:
        tek += 1
    t += 1

print(on_sayfa)
print(arka_sayfa)