import random
seed = random.randint(1, 1000000)
random.seed(seed)
print(f"seed: {seed}")
dek = list()

# dit zijn de variabelen
kleuren = ['groen', 'blauw', 'geel', 'rood']
cijfer = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
neemTwee = '+2'
beurtOverslaan = 'beurt overslaan'
volgorde = 'keer-om'
neemVier = '+4'
kiesKleur = 'kies'
spelerDict = {
}
stapel = list()
i = True
# hier word gevraagd voor het aantal spelers
while i == True:
    aantalSpelers = int(input('met hoeveel spelers wil je spelen? >> '))
    if aantalSpelers > 10:
        print('je kan maximaal met 10 spelers spelen')
    elif aantalSpelers > 1:
        i = False
    elif aantalSpelers <= 1:
        print('je hebt minimaal 2 spelers nodig om te spelen')


def dekMaken():
    # hier worden de speciale kaarten aangemaakt
    for x in range(2):
        for i in range(len(kleuren)):
            dek.append(kleuren[i]+"."+neemTwee)
            dek.append(kleuren[i]+"."+volgorde)
            dek.append(kleuren[i]+"."+beurtOverslaan)
        for y in range(2):
            dek.append("any." + kiesKleur)
            dek.append("any." + neemVier)

    # hier worden alle normale kaarten gemaakt
    for i in range(2):
        for x in range(len(cijfer)):
            dek.append(kleuren[0]+"."+cijfer[x])
            dek.append(kleuren[1]+"."+cijfer[x])
            dek.append(kleuren[2]+"."+cijfer[x])
            dek.append(kleuren[3]+"."+cijfer[x])
    for i in range(len(kleuren)):
        dek.append(kleuren[i]+'.0')
    random.shuffle(dek)


def dekDelen():
    # hier worden de kaarten aan het dek van de spelers toegevoegd
    for i in range(aantalSpelers):
        spelerDek = []
        for x in range(7):
            spelerDek.append(dek[0])
            dek.pop(0)
        spelerDict[f"speler{i}"] = spelerDek


def rondeSpelen():
    space = " "
    topCard = dek[0].split(".")
    input(f"de top kaart is {space.join(topCard)}")
    stapel = []
    for i in range(aantalSpelers):
        kaart = []
        print(f"Speler {i+1} is aan de beurt, kies je Kaart:")
        for x in range(len(spelerDict[f"speler{i}"])):
            kaart = spelerDict[f"speler{i}"][0].split(".")
            if kaart[0] == topCard[0] or kaart[1] == topCard[1]:
                stapel.append(".".join(topCard))
                topCard = kaart
                print(topCard)
                print(kaart)
                kaart.clear()
            else:
                print("kan niet")


dekMaken()
dekDelen()
rondeSpelen()
