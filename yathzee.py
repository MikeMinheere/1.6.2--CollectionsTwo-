import random
import time
import webbrowser
import collections
from collections import Counter

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

input('druk op enter om te starten >> ')
print('u gaat nu Yathzee spelen')
help = input('wilt u de spelregels weten? (J/N)').upper()
if help == 'J':
    webbrowser.open("https://www.dobbelstenenshop.nl/spelregels-yahtzee/")
else:()
time.sleep(2)
aantalDobbelstenen = 5
dobbelen = list()

def dobbelRollen(aantalDobbelstenen):
    for i in range(3):
        if len(dobbelen) > 0:
            print('dit zijn uw gerolde nummers:')
            time.sleep(1)
            print(*dobbelen, sep=", ")
            time.sleep(1)
            # hier kies je of je de dobbelsteen opnieuw wilt rollen of niet.
            for i in range(len(dobbelen)):
                dobbelsOpzijLeggen = input('wil je de dobbelsteen met nummer ' + str(dobbelen[i]) + ' apart leggen? [J/N] ')
                if dobbelsOpzijLeggen.upper() == 'J':
                    dobbelsOpzij.append(dobbelen[i])
                    deleteFromList.append(i)
                    aantalDobbelstenen -= 1
                else:()
        dobbelen.clear()
        # dit laat de overige dobbelstenen opnieuw dobbelen 
        for i in range(0,aantalDobbelstenen):
            dobbelcijfer = random.randint(1,6)
            dobbelen.append(dobbelcijfer)
        # dit verwijdert de dobbestenen uit de list wanneer ze opzij gelegd worden.
        for x in range(0, len(deleteFromList)):
            deleteFromList.pop(len(deleteFromList)-1)
for i in range(0,aantalDobbelstenen):
    dobbelcijfer = random.randint(1,6)
    dobbelen.append(dobbelcijfer)
dobbelsOpzij = list()
deleteFromList = list()

dobbelRollen(aantalDobbelstenen)
if len(dobbelen) > 0:
    dobbelsOpzij.append(*dobbelen,sep='')   
print()
time.sleep(1)
print('dit zijn de cijfers die jij opzij gelegd hebt:')
time.sleep(1)
print(*dobbelsOpzij, sep=", ")
keuze = ['eenen','tweeën','drieën','vieren','vijfen','zessen','three of a kind','four of a kind','full house','small straight','large straight','yathzee','chance']
time.sleep(1)
print()
print('je kan je score opslaan als: ' + str(keuze)+ ' ')
time.sleep(1)
print()
scoreOpslaan=input('type het woord in van de lijst van hoe je hem wilt opslaan>> ')
if scoreOpslaan == 'eenen':
    keuze.remove('eenen')
    a=0
    for i in range(len(dobbelsOpzij)):
        if dobbelsOpzij[a] == 1:
            een.append(dobbelsOpzij[a])
        a+=1
#dit voegt alle cijfers toe aan een aparte list om de score mee te berekenen
elif scoreOpslaan == 'tweeën' or scoreOpslaan == 'tweeen':
    keuze.remove('tweeën')
    a=0
    for i in range(len(dobbelsOpzij)):
        if dobbelsOpzij[a] == 2:
            twee.append(dobbelsOpzij[a])
        a+=1
elif scoreOpslaan == 'drieën' or scoreOpslaan == 'drieen':
    keuze.remove('drieën')
    a=0
    for i in range(len(dobbelsOpzij)):
        if dobbelsOpzij[a] == 3:
            drie.append(dobbelsOpzij[a])
        a+=1
elif scoreOpslaan == 'vieren':
    keuze.remove('vieren')
    a=0
    for i in range(len(dobbelsOpzij)):
        if dobbelsOpzij[a] == 4:
            vier.append(dobbelsOpzij[a])
        a+=1
elif scoreOpslaan == 'vijfen':
    keuze.remove('vijfen')
    a=0
    for i in range(len(dobbelsOpzij)):
        if dobbelsOpzij[a] == 5:
            vijf.append(dobbelsOpzij[a])
        a+=1
elif scoreOpslaan == 'zessen':
    keuze.remove('zessen')
    a=0
    for i in range(len(dobbelsOpzij)):
        if dobbelsOpzij[a] == 6:
            zes.append(dobbelsOpzij[a])
        a+=1
elif scoreOpslaan == 'three of a kind':
    keuze.remove('three of a kind')
    dup = {x for x in dobbelsOpzij if dobbelsOpzij.count(x) == 3}
    if len(dup) > 0:
        threeOfKind.append(dobbelsOpzij)
elif scoreOpslaan == 'four of a kind':
    keuze.remove('four of a kind')
    dup = {x for x in dobbelsOpzij if dobbelsOpzij.count(x) == 4}
    if len(dup) > 0:
        fourOfKind.append(dobbelsOpzij)
elif scoreOpslaan == 'full house':
    keuze.remove('full house')
    dup = {x for x in dobbelsOpzij if dobbelsOpzij.count(x) == 3}
    dup2 = {x for x in dobbelsOpzij if dobbelsOpzij.count(x) == 2}
    if len(dup) > 0 and len(dup2) > 0:
        fullHouse.append(dobbelsOpzij)
    print(fullHouse)
elif scoreOpslaan == 'small straight':
    keuze.remove('small straight')
    sStraight = False
    y = [0,0,0]
    for x in range(1,7):
        y[0] = dobbelsOpzij.count(x)
        y[1] = dobbelsOpzij.count(x+1)
        y[2] = dobbelsOpzij.count(x+2)
        if y[0] > 0 and y[1] > 0 and y[2] > 0:
            sStraight = True
elif scoreOpslaan == 'large straight':
    keuze.remove('large straight')
    lStraight = False
    y = [0,0,0,0]
    for x in range(1,7):
        y[0] = dobbelsOpzij.count(x)
        y[1] = dobbelsOpzij.count(x+1)
        y[2] = dobbelsOpzij.count(x+2)
        y[3] = dobbelsOpzij.count(x+3)
        if y[0] > 0 and y[1] > 0 and y[2] > 0:
            lStraight = True
elif scoreOpslaan == 'yathzee':
    keuze.remove('yathzee')
    yathzee.append(dobbelsOpzij)
elif scoreOpslaan == 'chance':
    keuze.remove('chance')
    chance.append(dobbelsOpzij)
    