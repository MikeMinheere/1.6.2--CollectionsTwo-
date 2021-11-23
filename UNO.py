i = True
while i==True:
    aantalSpelers=int(input('met hoeveel spelers wil je spelen? '))
    if aantalSpelers>1:
        i = False
    elif aantalSpelers<=1:
        print('je hebt minimaal 2 spelers nodig om te spelen')
