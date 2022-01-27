import random
seed = random.randint(1,1000000)
random.seed(seed)
print(f"seed: {seed}")
dek=list()

#dit zijn de variabelen 
kleuren=['groen','blauw','geel','rood']
cijfer=['1','2','3','4','5','6','7','8','9']
neemTwee=' +2 kaart'
beurtOverslaan='beurt overslaan kaart'
volgorde='keer-om kaart'
neemVier='+4 kaart'
kiesKleur='kies kaart'
spelers=list()
stapel=list()

speler1=list()
speler2=list()
speler3=list()
speler4=list()
speler5=list()
speler6=list()
speler7=list()
speler8=list()
speler9=list()
speler10=list()

i = True
# hier word gevraagd voor het aantal spelers
while i==True:
    aantalSpelers=int(input('met hoeveel spelers wil je spelen? >> '))
    if aantalSpelers>10:
        print('je kan maximaal met 10 spelers spelen')
    elif aantalSpelers>1:
        i = False
    elif aantalSpelers<=1:
        print('je hebt minimaal 2 spelers nodig om te spelen')
        i = False
#hier worden de speciale kaarten aangemaakt 
for x in range(2):
    for i in range(len(kleuren)):
        dek.append(kleuren[i]+"."+neemTwee)
for x in range(2):
    for i in range(len(kleuren)):
        dek.append(kleuren[i]+"."+beurtOverslaan)
for x in range(2):
    for i in range(len(kleuren)):
        dek.append(kleuren[i]+"."+volgorde)
for x in range(2):
    for i in range(len(kleuren)):
        dek.append(kleuren[i]+"."+kiesKleur)
for x in range(4):
    dek.append(kiesKleur)
for x in range(4):
    dek.append(neemVier)

#hier worden alle normale kaarten gemaakt 
for i in range(2):
    for x in range(len(cijfer)):
        dek.append(kleuren[0]+"."+cijfer[x])
    for x in range(len(cijfer)):
        dek.append(kleuren[1]+"."+cijfer[x])
    for x in range(len(cijfer)):
        dek.append(kleuren[2]+"."+cijfer[x])
    for x in range(len(cijfer)):
        dek.append(kleuren[3]+"."+cijfer[x])
for i in range(len(kleuren)):
    dek.append(kleuren[i]+'.0')
random.shuffle(dek)