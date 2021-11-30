import random
seed = random.randint(1,1000000)
random.seed(seed)
print(f"seed: {seed}")
dek=list()
kleuren=['groen ','blauw ','geel ','rood ']
cijfer=['1','2','3','4','5','6','7','8','9']
neemTwee='+2 kaart'
beurtOverslaan='beurt overslaan kaart'
volgorde='keer-om kaart'
neemVier='+4 kaart'
kiesKleur='kies kaart'
spelers=list()

i = True
while i==True:
    aantalSpelers=int(input('met hoeveel spelers wil je spelen? >> '))
    if aantalSpelers>10:
        print('je kan maximaal met 10 spelers spelen')
    elif aantalSpelers>1:
        i = False
    elif aantalSpelers<=1:
        print('je hebt minimaal 2 spelers nodig om te spelen')
for x in range(2):
    for i in range(len(kleuren)):
        dek.append(kleuren[i]+neemTwee)
for x in range(2):
    for i in range(len(kleuren)):
        dek.append(kleuren[i]+beurtOverslaan)
for x in range(2):
    for i in range(len(kleuren)):
        dek.append(kleuren[i]+volgorde)
for x in range(2):
    for i in range(len(kleuren)):
        dek.append(kleuren[i]+kiesKleur)
for i in range(2):
    for x in range(len(cijfer)):
        dek.append(kleuren[0]+cijfer[x])
    for x in range(len(cijfer)):
        dek.append(kleuren[1]+cijfer[x])
    for x in range(len(cijfer)):
        dek.append(kleuren[2]+cijfer[x])
    for x in range(len(cijfer)):
        dek.append(kleuren[3]+cijfer[x])
for i in range(len(kleuren)):
    dek.append(kleuren[i]+' 0')
random.shuffle(dek)
for x in range(aantalSpelers):
    spelers.append(list())
for i in range(aantalSpelers):
    for x in range(7):
        spelers[i].append(dek[x])
        del dek[x]
    print(*spelers[i],sep= " | ")
    print()
print(len(dek))
eersteKaart=dek[0]
print(eersteKaart)
