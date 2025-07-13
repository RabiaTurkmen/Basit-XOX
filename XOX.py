import random
alan=[]
for i in range(3):
    alan.append("_"*3)
for i in alan:
    print(" ".join(i))

# X-> ben O->Bilg.
while True:

    while True:
        satir = int(input("bir satir degeri giriniz:"))
        sutun = int(input("Bir sutun degeri giriniz:"))
        if alan[satir-1][sutun-1]!="_":
            print("Lutfen baska bir secim yapiniz.")
        else:
            break
    satir-=1
    sutun-=1
    gecici=alan[satir]
    gecici=gecici[0:sutun:]+"X"+gecici[sutun+1::]
    alan[satir]=gecici


    if (alan[0][0] == alan[0][1] == alan[0][2]=="0") or (alan[1][0] == alan[1][1] == alan[1][2]=="0") or (alan[2][0] == alan[2][1] == alan[2][2]=="0"):
        print("Bilgisayar kazandi.")
        break
    if (alan[0][0] == alan[0][1] == alan[0][2]=="X") or (alan[1][0] == alan[1][1] == alan[1][2]=="X") or (alan[2][0] == alan[2][1] == alan[2][2]=="X"):
        print("Sen kazandin.")
        break
    if (alan[0][0] == alan[1][0] == alan[2][0]=="0") or (alan[0][1] == alan[1][1] == alan[2][1]=="0") or (alan[0][2] == alan[1][2] == alan[2][2]=="0"):
        print("Bilgisayar kazandi.")
        break
    if (alan[0][0] == alan[1][0] == alan[2][0] == "X") or (alan[0][1] == alan[1][1] == alan[2][1] == "X") or (
            alan[0][2] == alan[1][2] == alan[2][2] == "X"):
        print("Sen kazandin.")
        break
    if (alan[0][0] == alan[1][1] == alan[2][2] == "0")  or (alan[0][2] == alan[1][1] == alan[2][0] == "0"):
        print("Bilgisayar kazandi.")
        break
    if (alan[0][0] == alan[1][1] == alan[2][2] == "X")  or (alan[0][2] == alan[1][1] == alan[2][0] == "X"):
        print("Sen kazandin.")
        break
    while True:
        satir=random.randint(0,2)
        sutun=random.randint(0,2)
        if alan[satir][sutun]=="_":
            break
        else:
            continue
    gecici=alan[satir]
    gecici=gecici[0:sutun:]+"0"+gecici[sutun+1::]
    alan[satir]=gecici
    for i in alan:
        print(" ".join(i))
