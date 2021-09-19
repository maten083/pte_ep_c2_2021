import random

#Játékosok(X)és(O)- kezdés
player12 = random.randint(0, 1)
if player12 == 0:
    player = "X"
else:
    player = "O"
print("Az",player,"-játékos kezd!")
print("A helyek lerakása mátrix-szerű megadással történik - pl.: 1. sor 2. oszlop!")

#A tábla létrehozása (mátrix)
tabla=[]
for i in range(3):
    sor = []
    for j in range(3):
        sor.append("-")
    tabla.append(sor)
for sor in tabla:
    for elem in sor:
        print(elem,end=" ")
    print()

#A létező tábla meghívása
def board():
    for sor in tabla:
        for elem in sor:
            print(elem,end=" ")
        print()

#Adatok bekérése a felhasználótól!
x = int(input("kérem a sor számát:\t"))
y = int(input("kérem az oszlop számát:\t"))

def fix_pont(x,y):     #Ha a hely nem foglalt csak akkor rajókja le az X-et/O-t!
    if tabla[x-1][y-1] == "-":
        tabla[x-1][y-1] = player
        board()
    else:
        print("Ez a hely foglalt!")
        board()
        x = int(input("kérem a sor számát:\t"))
        y = int(input("kérem az oszlop számát:\t"))

        fix_pont(x,y)
fix_pont(x,y)

#Váltás a másik játékosra úgy, hogy megnézzük volt-e győzelem
 #Vízszintes

win = None
gameover = 0
while win != True:
    for sor in tabla:
        if sor[0] == player and sor[1] == player and sor[2] == player:
            win = True
        #Függőleges
    oszlop = 0
    for sor in tabla:
         if sor[0] == player:
            oszlop += 1
         if oszlop == 3:
            win = True
    oszlop2 = 0
    for sor in tabla:
         if sor[1] == player:
             oszlop2 += 1
         if oszlop2 == 3:
            win = True
    oszlop3 = 0
    for sor in tabla:
         if sor[2] == player:
             oszlop3 += 1
         if oszlop3 == 3:
            win = True
        #Átlók
    if tabla[0][0] == player and tabla[1][1] == player and tabla[2][2] == player:
        win = True
    if tabla[2][0] == player and tabla[1][1] == player and tabla[0][2] == player:
        win = True

    if win:
        print(player,"győzött!")
        break

    if not win:
        gameover += 1
        #print(gameover)  meneteket számolja
        if gameover == 9:
            print("Döntetlen!")
            break
        if player == "X":
            player = "O"
            print(player,"következik")
        else:
            player = "X"
            print(player, "következik")
    x = int(input("kérem a sor számát:\t"))
    y = int(input("kérem az oszlop számát:\t"))
    fix_pont(x,y)