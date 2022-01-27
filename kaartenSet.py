import random
dek = list()
jokers = ['joker,', 'Joker,']
soorten = ['klaveren ', 'harten ', 'schoppen ', 'ruiten ']
cijfer = ['1,','2,','3,','4,','5,','6,','7,','8,','9,','10,','boer,','vrouw,','heer,','aas,']
for x in range (0,len(soorten)):
    for y in range(0,len(cijfer)):
        dek.append(soorten[x]+cijfer[y])
dek.append(jokers[0]);dek.append(jokers[1])
randomdek = list()
for x in range(0,len(dek)):
    randomnummer = random.randint(0,len(dek))
    randomdek.append(dek[randomnummer-1])
    dek.remove(dek[randomnummer-1])
zevenKaarten = (randomdek[0],randomdek[1],randomdek[2],randomdek[3],randomdek[4],randomdek[5],randomdek[6])
for lijstje in zevenKaarten:
    print(lijstje)
print()
printKaarten= ''
for x in range(7,54):
    printKaarten += randomdek[x]+" "
print(printKaarten)