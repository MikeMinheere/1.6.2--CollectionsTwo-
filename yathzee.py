import random
dobbelen = list()
dobbelsteen = ['1','2','3','4','5','6']
for i in range(0,5):
    dobbelcijfer = random.randint(0,5)
    dobbelen.append(dobbelsteen[dobbelcijfer])
print(*dobbelen, sep=", ")