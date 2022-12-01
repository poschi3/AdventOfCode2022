elfs = []

with open('input.txt') as file:
    currentMax = 0
    for calorie in file.readlines():
        if calorie.strip():
            currentMax += int(calorie)
        else:
            elfs.append(currentMax)
            currentMax = 0

elfs.sort(reverse=True)
print(elfs[0])
print(sum(elfs[:3]))
