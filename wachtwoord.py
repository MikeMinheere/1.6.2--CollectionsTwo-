import random
import string
import time

print('time to passwrd!!!!!1!!111!')
time.sleep(2)
print('processing...')
time.sleep(6)
print('process complete!')
time.sleep(1)
cijfer = ['1','2','3','4','5','6','7','8','9']
tekens = ['#','@','&','?','_','%','$']
wachtwoord = list()

print()
for i in range(random.randint(2,6)):
    hoofdletterList = list(string.ascii_uppercase)
    randomHoofdletters = random.randint(0,23)
    wachtwoord.append(hoofdletterList[randomHoofdletters])
for i in range(random.randint(4,7)):
    nummerList = ['1','2','3','4','5','6','7','8','9']
    randomCijfers = random.randint(0,8)
    wachtwoord.append(nummerList[randomCijfers])
for i in range(random.randint(3,3)):
    tekenList = ['#','@','&','?','_','%','$']
    randomTeken = random.randint(0,6)
    wachtwoord.append(tekenList[randomTeken])
while len(wachtwoord) != 24:
    kleineLetterList = list(string.ascii_lowercase)
    randomLetters = random.randint(0,23)
    wachtwoord.append(kleineLetterList[randomLetters])
random.shuffle(wachtwoord)
x = True
while x == True:
    if wachtwoord[0] in tekens or wachtwoord[23] in tekens or wachtwoord[0] in cijfer or wachtwoord[1] in cijfer or wachtwoord[2] in cijfer:
        random.shuffle(wachtwoord)
    else: print(*wachtwoord, sep="");x = False
print()
print()
time.sleep(60)