import pyperclip
import os

r = "r"
while r == "r":
    durum = int(input("Page per sheet (1,2,4 or whatever you want) :"))
    sayfa = int(input("Number of pages of the document :"))
    on_sayfa = ""
    arka_sayfa = ""
    tek = 0
    t = 1

    while t <= sayfa:
        if tek % 2 == 0:
            on_sayfa += str(t) + ","
        else:
            arka_sayfa += str(t) + ","

        if t % durum == 0:
            tek += 1
        t += 1

    print("\n\nFront pages:" ,on_sayfa[:-1:])
    pyperclip.copy(on_sayfa[:-1:])
    input("\nFront pages are saved on clipboard. Press ENTER to continue with back pages.")
    print("\n\nBack pages:" ,arka_sayfa[:-1:])
    pyperclip.copy(arka_sayfa[:-1:])

    r = input("\nBack pages are saved on clipboard.\nWrite 'r' to continue or Press ENTER without writing anything to quit.")
    os.system('cls' if os.name ==  'nt' else 'clear')