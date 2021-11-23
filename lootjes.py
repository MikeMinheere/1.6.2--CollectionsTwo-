import random
naamlist=list()
lootjesgeven=list()
x = True 
while x==True:
    naam = input('voer hier een naam in voor lootjes trekken. type "klaar" als je geen namen meer wilt toevoegen >> ')
    if naam == 'klaar':
        if len(naamlist)<2:
            print('sorry, je moet minimaal 2 namen hebben om lootjes te kunnen trekken')
        else:x=False
    elif naam == '':
        pass
    elif naam != 'klaar':
        naamlist.append(naam)
        naamlist=list(dict.fromkeys(naamlist))
naamlist2 = list(naamlist)
random.shuffle(naamlist2)

for y in range(5):
    for i in range(len(naamlist)):
        if naamlist[i] == naamlist[i]:
            random.shuffle(naamlist)
for i in range(len(naamlist)):
    print(naamlist[i]+' - '+naamlist2[i])