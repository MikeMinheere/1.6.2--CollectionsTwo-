import random
import time
import webbrowser
import collections
from collections import Counter
Score=0
een=list()
twee=list()
drie=list()
vier=list()
vijf=list()
zes=list()
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
    for i in range(3):
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

dobbelsOpzij = list()
deleteFromList = list()
keuze = ['eenen','tweeën','drieën','vieren','vijfen','zessen','three of a kind','four of a kind','full house','small straight','large straight','yathzee','chance']
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
        scoreOpslaan=input('type het woord in van de lijst van hoe je hem wilt opslaan>> ')
        if scoreOpslaan == 'eenen':
            plek = checklist(keuze, scoreOpslaan) 
            if plek != -1:
                keuze.pop(plek)
                a=0
                for i in range(len(dobbelsOpzij)):
                    if dobbelsOpzij[a] == 1:
                        een.append(dobbelsOpzij[a])
                    a+=1
                Score += len(een)*1
                dobbelsOpzij.clear()
                x=False
        #dit voegt alle cijfers toe aan een aparte list om de score mee te berekenen
        elif scoreOpslaan == 'tweeën':
            plek = checklist(keuze, scoreOpslaan) 
            if plek != -1:
                keuze.pop(plek)
                a=0
                for i in range(len(dobbelsOpzij)):
                    if dobbelsOpzij[a] == 2:
                        twee.append(dobbelsOpzij[a])
                    a+=1
                Score += len(twee)*2
                dobbelsOpzij.clear()
                x=False
        elif scoreOpslaan == 'drieën':
            plek = checklist(keuze, scoreOpslaan) 
            if plek != -1:
                keuze.pop(plek)
                a=0
                for i in range(len(dobbelsOpzij)):
                    if dobbelsOpzij[a] == 3:
                        drie.append(dobbelsOpzij[a])
                    a+=1
                Score += len(drie)*3
                dobbelsOpzij.clear()
                x=False
        elif scoreOpslaan == 'vieren':
            plek = checklist(keuze, scoreOpslaan) 
            if plek != -1:
                keuze.pop(plek)
                a=0
                for i in range(len(dobbelsOpzij)):
                    if dobbelsOpzij[a] == 4:
                        vier.append(dobbelsOpzij[a])
                    a+=1
                Score += len(vier)*4
                dobbelsOpzij.clear()
                x=False
        elif scoreOpslaan == 'vijfen':
            plek = checklist(keuze, scoreOpslaan) 
            if plek != -1:
                keuze.pop(plek)
                a=0
                for i in range(len(dobbelsOpzij)):
                    if dobbelsOpzij[a] == 5:
                        vijf.append(dobbelsOpzij[a])
                    a+=1
                Score += len(vijf)*5
                dobbelsOpzij.clear()
                x=False
        elif scoreOpslaan == 'zessen':
            plek = checklist(keuze, scoreOpslaan) 
            if plek != -1:
                keuze.pop(plek)
                a=0
                for i in range(len(dobbelsOpzij)):
                    if dobbelsOpzij[a] == 6:
                        zes.append(dobbelsOpzij[a])
                    a+=1
                Score += len(zes)*6
                dobbelsOpzij.clear()
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
                y = [0,0,0,0]
                for x in range(1,7):
                    y[0] = dobbelsOpzij.count(x)
                    y[1] = dobbelsOpzij.count(x+1)
                    y[2] = dobbelsOpzij.count(x+2)
                    y[3] = dobbelsOpzij.count(x+3)
                    if y[0] > 0 and y[1] > 0 and y[2] > 0 and y[3] > 0:
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
                for x in range(1,7):
                    y[0] = dobbelsOpzij.count(x)
                    y[1] = dobbelsOpzij.count(x+1)
                    y[2] = dobbelsOpzij.count(x+2)
                    y[3] = dobbelsOpzij.count(x+3)
                    y[4] = dobbelsOpzij.count(x+4)
                    if y[0] > 0 and y[1] > 0 and y[2] > 0 and y[3] > 0 and y[4] > 0:
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
                    yatz = True
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
    print(Score)