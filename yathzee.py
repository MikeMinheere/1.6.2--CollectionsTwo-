import random
aantalDobbelstenen = 5
dobbelen = list()
for i in range(0,aantalDobbelstenen):
    dobbelcijfer = random.randint(1,6)
    dobbelen.append(dobbelcijfer)
print(*dobbelen, sep=", ")
for i in range(len(dobbelen)):
    dobbelsOpzij = input('wil je de dobbelsteen met nummer ' + str(dobbelen[i]) + ' apart leggen? [J/N] ')
    if dobbelsOpzij.upper == 'J':