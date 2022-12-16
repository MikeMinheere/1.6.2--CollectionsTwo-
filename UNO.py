import random
seed = random.randint(1, 1000000)
random.seed(seed)
print(f"seed: {seed}")
dek = list()

# dit zijn de variabelen
kleuren = ['groen', 'blauw', 'geel', 'rood']
cijfer = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
neemTwee = '+2'
beurtOverslaan = 'beurt-overslaan'
volgorde = 'keer-om'
neemVier = '+4'
kiesKleur = 'kies-kleur'
spelerDict = {
}
pestKaarten = [neemTwee, beurtOverslaan, volgorde, neemVier, kiesKleur, volgorde]
stapel = list()
i = True
# hier word gevraagd voor het aantal spelers
while i == True:
    aantalSpelers = int(input('met hoeveel spelers wil je spelen? >>> '))
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
    i = True
    space = " "
    topCard = dek[0].split(".")
    while i == True:
        if any(topCard[1] in s for s in pestKaarten):
            random.shuffle(dek)
            topCard = dek[0].split(".")
            del dek[0]
        else:
            i = False
    stapel = []
    y = True
    while y == True:
        #de loop met aantalspelers is voor de beurt van iedere spelen, dus 1 loop, is 1 speler zijn beurt.
        for i in range(aantalSpelers):
            input(f"de top kaart is {space.join(topCard)} ")
            print(f"Speler {i+1} is aan de beurt, kies je Kaart, of pak een nieuwe:")
            print(", ".join(spelerDict[f"speler{i}"])+ ", pakken")
            kaartSelectie = input(">>> ")
            if kaartSelectie == "pakken".lower():
                spelerDict[f"speler{i}"].append(dek[0])
                del dek[0]
            else: 
                kaart = kaartSelectie.split(".")
                if kaart[0] == topCard[0] or kaart[1] == topCard[1] or kaart[0] == "any":
                    spelerDict[f"speler{i}"]
                    stapel.append(".".join(topCard))
                    for x in range(len(spelerDict[f"speler{i}"])):
                        if ".".join(kaart) == spelerDict[f"speler{i}"][x]:
                            del spelerDict[f"speler{i}"][x]
                            break
                    if kaart[0] == "any":
                        kies = input("kies een kleur: groen, rood, geel, blauw. >>> ")
                        topCard = [kies, kaart[1]]
                    else:
                        topCard = kaart
                    del kaart

                else:
                    print("kan niet")
                if len(spelerDict[f"speler{i}"]) <= 0:
                    y = False


dekMaken()
dekDelen()
rondeSpelen()
