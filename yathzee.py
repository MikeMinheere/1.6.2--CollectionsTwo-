import random
import time
import webbrowser
import collections
from collections import Counter
Score=0
scoreDict = {
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    'bonus':0    
}
cijfer = [1,2,3,4,5,6]
alGehadDict = {
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0
}

def checklist(keuze, scoreOpslaan):
    nummer = -1
    for x in range(len(keuze)):
        if keuze[x] == scoreOpslaan:
            nummer = x
    return nummer
input('druk op enter om te starten >> ')
print('u gaat nu Yathzee spelen')
help = input('wilt u de spelregels weten? (J/N)').upper()
if help == 'J':
    webbrowser.open("https://www.dobbelstenenshop.nl/spelregels-yahtzee/")
else:()
time.sleep(1)
aantalDobbelstenen = 5
dobbelen = list()
restDobbels=list()

def dobbelRollen(aantalDobbelstenen):
    for i in range(0,aantalDobbelstenen):
        dobbelcijfer = random.randint(1,6)
        dobbelen.append(dobbelcijfer)
    i = 0
    for i in range(2):
        if len(dobbelen) > 0:
            print('dit zijn uw gerolde nummers:')
            time.sleep(1)
            print(*dobbelen, sep=", ")
            time.sleep(1)
            # hier kies je of je de dobbelsteen opnieuw wilt rollen of niet.
            for x in range(len(dobbelen)):
                dobbelsOpzijLeggen = input('wil je de dobbelsteen met nummer ' + str(dobbelen[x]) + ' apart leggen? [J/N] ')
                if dobbelsOpzijLeggen.upper() == 'J':
                    dobbelsOpzij.append(dobbelen[x])
                    deleteFromList.append(x)
                    aantalDobbelstenen -= 1
                else:restDobbels.append(dobbelen[x])
        dobbelen.clear()
        # dit laat de overige dobbelstenen opnieuw dobbelen 
        for i in range(0,aantalDobbelstenen):
            dobbelcijfer = random.randint(1,6)
            dobbelen.append(dobbelcijfer)
        # dit verwijdert de dobbestenen uit de list wanneer ze opzij gelegd worden.
        for x in range(0, len(deleteFromList)):
            deleteFromList.pop(len(deleteFromList)-1)
    dobbelen.clear()

def scoreOptellen():
    if sum(scoreDict.values())>=63:
        scoreDict['bonus'] += 35
    print('\n Uw eindscore:')
    for key, value in scoreDict.items():
        print(key, ' : ', value)

dobbelsOpzij = list()
deleteFromList = list()
keuze = ['1 ','2 ','3 ','4 ','5 ','6']
for i in range(2):
    dobbelsOpzij.clear()
    dobbelRollen(aantalDobbelstenen)
    if len(dobbelen) > 0:
        dobbelsOpzij.append(dobbelen)   
    if len(dobbelsOpzij)< 5:
        while len(dobbelsOpzij)<5:
            dobbelcijfer = random.randint(1,6)
            dobbelsOpzij.append(dobbelcijfer)
    print()
    time.sleep(1)
    print('dit zijn de cijfers die jij opzij gelegd hebt:')
    time.sleep(1)
    print(*dobbelsOpzij, sep=", ")
    time.sleep(1)
    print()
    print('je kan je score opslaan als: ' + str(keuze)+ ' ')
    time.sleep(1)
    print()
    x=True 
    while x == True:
        scoreOpslaan=int(input('type het cijfer van de lijst van hoe je hem wilt opslaan>> '))
        if alGehadDict[str(scoreOpslaan)]<1:
            alGehadDict[str(scoreOpslaan)]+=1
            for i in range(len(dobbelsOpzij)):
                if int(dobbelsOpzij[i])==int(scoreOpslaan):
                    scoreDict[str(cijfer[scoreOpslaan-1])]+=cijfer[scoreOpslaan-1]
                x=False
        else:print('cijfer al gehad')
scoreOptellen() 