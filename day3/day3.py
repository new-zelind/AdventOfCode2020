array = []
rows = 0 # total rows

for line in open("input", "r"):
    array.append(list(line.split('\n')[0]))
    rows += 1

currCol = 0 # current column access
ans1 = 0 # answer
ans2 = ans3 = ans4 = ans5 = 0

for currRow in range(323):
    currCol %= 31
    if array[currRow][currCol] == "#":
        ans1 += 1
    currCol += 3
currCol = 0

for currRow in range(323):
    currCol %= 31
    if array[currRow][currCol] == "#":
        ans2 += 1
    currCol += 1
currCol = 0

for currRow in range(323):
    currCol %= 31
    if array[currRow][currCol] == "#":
        ans3 += 1
    currCol += 5
currCol = 0

for currRow in range(323):
    currCol %= 31
    if array[currRow][currCol] == "#":
        ans4 += 1
    currCol += 7
currCol = 0

for currRow in range(0, 323, 2):
    currCol %= 31
    if array[currRow][currCol] == "#":
        ans5 += 1
    currCol += 1

ans = ans1 * ans2 * ans3 * ans4 * ans5

print(ans)