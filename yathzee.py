import random
import time

een=list()
twee=list()
drie=list()
vier=list()
vijf=list()
zes=list()
threeOfKind=list()
fourOfKind=list()
fullHouse=list()
sStraight=list()
lStraight=list()
yathzee=list()
chance=list()

input('druk op enter om te starten >> ')
print('u gaat nu Yathzee spelen')
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
scoreOpslaan=input('type het woord in van de lijst van hoe je hem wilt opslaan>> ')
if scoreOpslaan == 'eenen':
    keuze.remove('eenen')
    a=0
    for i in range(len(dobbelsOpzij)):
        if dobbelsOpzij[a] == 1:
            een.append(dobbelsOpzij[a])
        a+=1
elif scoreOpslaan == 'tweeën' or scoreOpslaan == 'tweeen':
    keuze.remove('tweeën')
    a=0
    for i in range(len(dobbelsOpzij)):
        if dobbelsOpzij[a] == 2:
            twee.append(dobbelsOpzij[a])
        a+=1
elif scoreOpslaan == 'drieën' or scoreOpslaan == 'drieen':
    keuze.remove('drieën')
    drie.append(dobbelsOpzij)
elif scoreOpslaan == 'vieren':
    keuze.remove('vieren')
    vier.append(dobbelsOpzij)
elif scoreOpslaan == 'vijfen':
    keuze.remove('vijfen')
    vijf.append(dobbelsOpzij)
elif scoreOpslaan == 'zessen':
    keuze.remove('zessen')
    zes.append(dobbelsOpzij)
elif scoreOpslaan == 'three of a kind':
    keuze.remove('three of a kind')
    threeOfKind.append(dobbelsOpzij)
elif scoreOpslaan == 'four of a kind':
    keuze.remove('four of a kind')
    fourOfKind.append(dobbelsOpzij)
elif scoreOpslaan == 'full house':
    keuze.remove('full house')
    fullHouse.append(dobbelsOpzij)
elif scoreOpslaan == 'small straight':
    keuze.remove('small straight')
    sStraight.append(dobbelsOpzij)
elif scoreOpslaan == 'large straight':
    keuze.remove('large straight')
    lStraight.append(dobbelsOpzij)
elif scoreOpslaan == 'yathzee':
    keuze.remove('yathzee')
    yathzee.append(dobbelsOpzij)
elif scoreOpslaan == 'chance':
    keuze.remove('chance')
    chance.append(dobbelsOpzij)
print(*een,sep=", ")