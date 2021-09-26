#átlagosan 365 egy év. 31536000 86400 3600 60 1
#mp convert
#m = 1   #1
#p = m*60 #60
#o = p*60 #3600
#n = o*24 #86400
#e = n*365 #31536000
#bekérés
s = int(input("adja meg a másodperceket:"))

if s < 0 or type(s) == str:
    print("0-nál nagyobb egész számot kell megadnia!")
#átváltás
mp = s
perc = int(s/60)
ora = int(perc/60)
nap = int(ora/24)
ev = int(nap/365)

name=['year', 'day', 'hour', 'minute', 'second']
time= [0, 0, 0, 0, 0]

time[0]=ev
time[1]=(nap-(ev*365))
time[2]=(ora-(nap*24))
time[3]=(perc-(ora*60))
time[4]=(s-(perc*60))

output_string = ""
last_not_null = -1
for i in range(4,-1,-1):
    if time[i] > 0:
        last_not_null = i
        break

notnull = 0
for elem in time:
    if elem == 0:
        notnull += 1

for index in range(5):
    if index == last_not_null and notnull != 4:
        output_string = output_string + "and "
    if time[index] == 1:
        output_string = output_string + str(time[index]) + " " + name[index] + " "
    elif time[index] > 1:
        output_string = output_string + str(time[index]) + " " + name[index] + "s "
    elif time[index] == 0:
        output_string = output_string+""

if s<= 59:
    if s == 1:
        print(s, "second")
    elif s == 0:print("now")
    else: print(s, "seconds")
if s > 59:
    print(output_string)