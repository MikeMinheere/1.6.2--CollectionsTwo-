import random
import time

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