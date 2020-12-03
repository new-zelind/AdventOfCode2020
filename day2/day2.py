from collections import namedtuple

Password = namedtuple('Password', ['hi', 'lo', 'letter', 'password'])
passList = []

with open("input", "r") as f:
    line = f.read()
    for l in line.split('\n'):
        max = l.split('-')[0]
        min = (l.split('-')[1]).split(' ')[0]
        letter = (l.split(' ')[1])[:-1]
        password = l.split(' ')[2]

        inputInfo = []
        inputInfo.append(min)
        inputInfo.append(max)
        inputInfo.append(letter)
        inputInfo.append(password)
        
        newPassword = Password._make(inputInfo)
        passList.append(newPassword)

total = 0

for p in passList:
    i1 = int(p.hi)
    i2 = int(p.lo)

    letter = p.letter
    password = p.password

    p1 = password[i1-1]
    p2 = password[i2-1]

    if (p1 == letter or p2 == letter) and p1 != p2:
        total += 1

print(total)