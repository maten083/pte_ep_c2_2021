szam = input("Adja meg milyen számot akar beolvasni:\t")
szamrend1 = int(input("Adja meg milyen számrendszerben akar beolvasni(2,8,10,16):\t"))
szamrend2 = int(input("Adja meg milyen számrendszerbe akarja kapni az eredményt(2,8,10,16):\t"))
#számrendszerek: 2,8,10,16
#1.) függvények:
def binary(n):
    b = bin(n)
    b1 = int(b[2:])
    return b1
def octo(n):
    b = oct(n)
    b1 = int(b[2:])
    return b1
def hexa(n):
    b = hex(n)
    b1 = str(b[2:])
    return b1

if szamrend1 == szamrend2:
    print(szam)

if szamrend1 == 10 and szamrend2 == 2:
    print(binary(szam))
if szamrend1 == 10 and szamrend2 == 8:
    print(octo(szam))
if szamrend1 == 10 and szamrend2 == 16:
    print(hexa(szam))
if szamrend1 == 8 and szamrend2 == 16:
    szam = int(szam,8)
    print(hexa(szam))
if szamrend1 == 8 and szamrend2 == 10:
    szam = int(szam,8)
    print(szam)
if szamrend1 == 8 and szamrend2 == 2:
    szam = int(szam,8)
    print(binary(szam))
if szamrend1 == 2 and szamrend2 == 16:
    szam = int(szam,2)
    print(hexa(szam))
if szamrend1 == 2 and szamrend2 == 10:
    szam = int(szam,2)
    print(szam)
if szamrend1 == 2 and szamrend2 == 8:
    szam = int(szam,2)
    print(octo(szam))
if szamrend1 == 16 and szamrend2 == 10:
    szam = int(szam,16)
    print(szam)
if szamrend1 == 16 and szamrend2 == 8:
    szam= int(szam,16)
    print(octo(szam))
if szamrend1 == 16 and szamrend2 == 2:
    szam = int(szam,16)
    print(binary(szam))