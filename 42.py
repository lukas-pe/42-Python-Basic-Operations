  #1
#print("Hello world")

#2
#vorname = input("Gib deinen Vornamen ein")
#print(f"Hallo, {vorname}")

#3
#x = 3.1415
#print(x)
#print(type(x))

#4
#text = "10"
#print(float(text))
#print(int(text))

#5
#x = 3.1415
#print(round(x, 2))

#6
#eingabe = input("Gib irgendwas ein")
#print(eingabe)
#print(type(eingabe))

#7
#text = "Hallo wie geths dir denn heute so"
#print(len(text))

#8
#print(bool(0))
#print(bool(1))

#9
#a = 3.1415
#print(isinstance(a, float))

#10
#print(3+2*4-5)

#11


#12 nicht fertig
#minuten = 135
#stunden = 135 // 60
#rest = minuten % 60
#
#print("stunden  stunden + rest + minuten")

#13
#eingabe = int(input("Gib eine Zahl ein"))
#print(eingabe * 2)

#14
#a = 3
#a += 3
#print(a)

#15
#e = int(input("Gib eine Zahl ein"))
#
#if e % 2 == 0:
#    print("Die Zahl ist gerade")
#else:
#    print("Die Zahl ist ungerade")

#16
#z = 12
#int(input("Gib eine Zahl ein"))
#
#if z % 2 == 0 and z % 3 == 0:
#    print("DIe Zahl ist durch 2 und 3 teilbar")
#
#else:
#    print("Nope, geht nicht")

#17

#a = 14
#b = 14
#
#if a > b:
#    print("a ist größer als b")
#
#elif a < b:
#    print("a ist kleiner als b")
#
#else:
#    print("DIe zahlen sind gleich groß")

#18
#a = "Hallo"
#b = "Welt"
#
#print(a + "-" + b)

#19
#h = "hALLo"
#
#print(h.upper())
#print(h.lower())

#20
#wort = "wurstbrot"
#
#print(wort[0])
#print(wort[-1])

#21
#wort = "wurstbrot"
#
#for c in wort:
#    print(c)

#22
#text = "Programmieren"
#print(text[-3])

#23
#print(True and not False)

#24
#a = True
#print(not a)

#25
#eingabe = int(input("Gib eine Zahl ein"))
#
#if eingabe > 0:
#    print("Positiv")
#
#elif eingabe < 0:
#    print("Negativ")
#else:
#    print("Die Zahl ist null")

#26
#alter = int(input("Wie alt bist du?"))
#if alter >= 18:
#    print("DU bist volljährig")
#elif alter < 18 and alter >= 0:
#    "Du bist minderjährig"
#else:
#    print("Du wurdest noch nicht geboren")

#27

#for zahl in range(1,10):
#    print(zahl)

#28
#for zahl in range(5,43):
#    print(zahl)

#29

#for zahl in range(0,43,2):
#    print(zahl)

#30

#eing = int(input("Gin eine Zahl ein die größer als 0 ist"))
#
#for zahl in range(0,eing + 1):
#    print(zahl)

#31 nicht fertig
#eingabe = int(input("Gib eine Zahl ein"))
#
#while eingabe != 0:
#    eingabe = int("Gib eine neue Zahl ein")

#32
#name = str(input("Gib deinen Namen ein: "))
#
#while name != "Wilfried":
#    name = str(input("Gib einen neuen Namen ein: "))

#33
#liste = [1,2,3,4]    
#
#print(liste[1])
#print(len(liste))

#34
#wörterbuch = {
#    "Name":"Wilfried",
#    "Alter":"36"
#}
#
#print(wörterbuch)

#37
#liste = [1,2,2,3,4,4,4]
#
#liste = list(set(liste))
#
#print(liste)

#38

#def begruesse():
#    print("Hallo, willkommen")
#
#begruesse()

#39

#def quadrat(zahl):
#    print(zahl * zahl)
#
#quadrat(6)

#40

#def ist_gerade(zahl):
#    if zahl % 2 == 0:
#        return True
#    else:
#        return False
#
#ist_gerade(2)

#41 

#def ist_ungerade(zahl):
#    if zahl % 2 != 0:
#        return True
#    else:
#        return False

#42

#def addiere(a,b):
#    return a + b
#
#ergebnis = addiere(5,3)
#
#print(ergebnis)

#zahlen = [10,20,30]

for i in range(5):
    if i ==3:
        continue

    print(i)
