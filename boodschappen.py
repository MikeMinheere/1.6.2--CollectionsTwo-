print()
i = True
boodschappen = set()
print('type hier iets om een item aan uw boodschappenlijstje toe te voegen, en type ook hoeveel je van dit item wilt.')
while i == True:
    boodschappen.add(input('>> '))
    opnieuw = input('als je opnieuw een item wilt toevoegen, klik dan op enter. ')
    if opnieuw != '':
        i = False
print()
for lijstje in boodschappen:
    print(lijstje)
print()