#dict-be 5 felhasználónév telefonszámmal
szamnev = {}
def szotar() -> dict:
    szamnev = {}
    szamnev = szamnev.copy()
    try:
        count = 0
        while count != 3:
            nev = input("Adjon meg egy nevet: ")  # KULCS
            szam = int(input("Adjon meg egy telefonszámot: "))  # ÉRTÉK
            szamnev[nev] = szam
            count += 1
        print(szamnev)
    except ValueError:
        print("Hiba!")
    return szamnev

szamnev=szotar()


def ABC(szamnev: dict):
    dic_elemek = szamnev.items()
    sorted_items = sorted(dic_elemek)
    return sorted(sorted_items)

print("A rendezett lista: ",ABC(szamnev))

def lekerdezes(x: str):
    x = input("Adja meg a nevet: ")
    index = 0
    T = 0
    for sor in szamnev:
        if x == sor: #mivel 5 nevet kérünk be
            print("c -",szamnev[x])
            T = 1
    if T == 0:
        print("Nincs ilyen kulcs!")
        index += 1

lekerdezes(szamnev)