import random
import time
import webbrowser
import collections
from collections import Counter
Score=0
scoreDict = {
    'een':0,
    'twee':0,
    'drie':0,
    'vier':0,
    'vijf':0,
    'zes':0,
    'bonus':0
    
}
threeOfKind=list()
fourOfKind=list()
fullHouse=list()
lStraight=list()
yathzee=list()
chance=list()

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
time.sleep(2)
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
keuze = ['1','2','3','4','5','6','three of a kind','four of a kind','full house','small straight','large straight','yathzee','chance']
for i in range(13):
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
        scoreOpslaan=input('type het woord in van de lijst van hoe je hem wilt opslaan>> ').lower()
        if scoreOpslaan == '1':
            for i in range(len(dobbelsOpzij)):
                if int(dobbelsOpzij[i])==1:
                    scoreDict['een']+=1
                    x=False
        elif scoreOpslaan == '2':
            for i in range(len(dobbelsOpzij)):
                if int(dobbelsOpzij[i])==2:
                    scoreDict['twee']+=2
                    x=False
        elif scoreOpslaan == '3':
            for i in range(len(dobbelsOpzij)):
                if int(dobbelsOpzij[i])==3:
                    scoreDict['drie']+=3
                    x=False
        elif scoreOpslaan == '4':
            for i in range(len(dobbelsOpzij)):
                if int(dobbelsOpzij[i])==4:
                    scoreDict['vier']+=4
                    x=False
        elif scoreOpslaan == '5':
            for i in range(len(dobbelsOpzij)):
                if int(dobbelsOpzij[i])==5:
                    scoreDict['vijf']+=5
                    x=False
        elif scoreOpslaan == '6':
            for i in range(len(dobbelsOpzij)):
                if int(dobbelsOpzij[i])==6:
                    scoreDict['zes']+=6
                    x=False
        elif scoreOpslaan == 'three of a kind':
            plek = checklist(keuze, scoreOpslaan) 
            if plek != -1:
                keuze.pop(plek)
                dup = {x for x in dobbelsOpzij if dobbelsOpzij.count(x) == 3}
                if len(dup) > 0:
                    threeOfKind.append(dobbelsOpzij)
                    Score += sum(dobbelsOpzij)
                dobbelsOpzij.clear()
                x=False
        elif scoreOpslaan == 'four of a kind':
            plek = checklist(keuze, scoreOpslaan) 
            if plek != -1:
                keuze.pop(plek)
                dup = {x for x in dobbelsOpzij if dobbelsOpzij.count(x) == 4}
                if len(dup) > 0:
                    fourOfKind.append(dobbelsOpzij)
                    Score += sum(dobbelsOpzij)
                dobbelsOpzij.clear()
                x=False
        elif scoreOpslaan == 'full house':
            plek = checklist(keuze, scoreOpslaan) 
            if plek != -1:
                keuze.pop(plek)
                full = False
                dup = {x for x in dobbelsOpzij if dobbelsOpzij.count(x) == 3}
                dup2 = {x for x in dobbelsOpzij if dobbelsOpzij.count(x) == 2}
                if len(dup) > 0 and len(dup2) > 0:
                    fullHouse.append(dobbelsOpzij)
                    full = True
                if full == True:
                    Score += 25
                dobbelsOpzij.clear()
                x=False
        elif scoreOpslaan == 'small straight':
            plek = checklist(keuze, scoreOpslaan) 
            if plek != -1:
                keuze.pop(plek)
                sStraight = False
                y = [0,0,0,0,0] 
                y[0] = dobbelsOpzij.count(x)
                y[1] = dobbelsOpzij.count(x+1)
                y[2] = dobbelsOpzij.count(x+2)
                y[3] = dobbelsOpzij.count(x+3)
                if (y[0] >= 0 and y[1] > 0 and y[2] > 0 and y[3] > 0)or(y[2]==2):
                    sStraight = True
                if sStraight == True: 
                    Score += 30
                dobbelsOpzij.clear()
                x=False
        elif scoreOpslaan == 'large straight':
            plek = checklist(keuze, scoreOpslaan) 
            if plek != -1:
                keuze.pop(plek)
                lStraight = False   
                y = [0,0,0,0,0]
                y[0] = dobbelsOpzij.count(x)
                y[1] = dobbelsOpzij.count(x+1)
                y[2] = dobbelsOpzij.count(x+2)
                y[3] = dobbelsOpzij.count(x+3)
                y[4] = dobbelsOpzij.count(x+4)

                if y[0] >= 0 and y[1] > 0 and y[2] > 0 and y[3] > 0 and y[4] > 0 :
                    lStraight = True
                if lStraight == True:
                    Score += 40
                dobbelsOpzij.clear()
                x=False
        elif scoreOpslaan == 'yathzee':
            plek = checklist(keuze, scoreOpslaan) 
            if plek != -1:
                keuze.pop(plek)
                dup = {x for x in dobbelsOpzij if dobbelsOpzij.count(x) == 5}
                yathz = False
                if len(dup) > 0:
                    yathz = True
                if yathz == True:
                    Score += 50
                dobbelsOpzij.clear()
                x=False
        elif scoreOpslaan == 'chance':
            plek = checklist(keuze, scoreOpslaan) 
            if plek != -1:
                keuze.pop(plek)
                Score += sum(dobbelsOpzij)
                dobbelsOpzij.clear()
                x=False
        else:print('sorry dat snap ik niet')
        dobbelsOpzij.clear()
