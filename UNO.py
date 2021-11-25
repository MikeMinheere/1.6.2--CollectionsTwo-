import random

i = True
while i==True:
    aantalSpelers=int(input('met hoeveel spelers wil je spelen? >> '))
    if aantalSpelers>10:
        print('je kan maximaal met 10 spelers spelen')
    elif aantalSpelers>1:
        i = False
    elif aantalSpelers<=1:
        print('je hebt minimaal 2 spelers nodig om te spelen')
dek=list()
kleuren=['groen ','blauw ','geel ','rood ']
cijfer=['1','2','3','4','5','6','7','8','9']
neemTwee='+2 kaart'
beurtOverslaan='beurt overslaan kaart'
volgorde='omdraaien kaart'
for i in range(len(kleuren)):
    for x in range(len(cijfer)):
        dek.append(kleuren[i]+cijfer[x])
random.shuffle(dek)
print(*dek,sep=' | ')
