# part 1

array = []
for num in open("input", "r"):
    array.append(int(num))

num1 = num2 = 0
for i in range(len(array)):
    for j in range(len(array)):
        if array[i] + array[j] == 2020:
            num1 = array[i]
            num2 = array[j]

print(num1 * num2)

# part 2
num1 = num2 = num3 = 0
for i in range(len(array)):
    for j in range(len(array)):
        for k in range(len(array)):
            if array[i] + array[j] + array[k] == 2020:
                num1 = array[i]
                num2 = array[j]
                num3 = array[k]

print(num1 * num2 * num3)