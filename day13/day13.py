def compare(left, right):
    r_index = -1

    for l in left:
        r_index += 1
        if r_index >= len(right):
            return -1

        r = right[r_index]
        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return 1
            elif l > r:
                return -1

        elif isinstance(l, list) and isinstance(r, list):
            c = compare(l, r)
            if c != 0:
                return c
        elif isinstance(l, int) and isinstance(r, list):
            c = compare([l], r)
            if c != 0:
                return c
        elif isinstance(l, list) and isinstance(r, int):
            c = compare(l, [r])
            if c != 0:
                return c
    
    if isinstance(left, list) and isinstance(right, list):
        if len(left) < len(right):
            return 1

    return 0

        
input = []
with open('day13/input.txt') as file:
    for line in file.readlines():
        if line.strip() != "":
            input.append(eval(line))

index = 0
sum = 0
while len(input) > 0:
    index += 1
    left = input.pop(0)
    right = input.pop(0)
    c = compare(left, right)
    if c == 1:
        sum += index
print(sum)


input = []
with open('day13/input.txt') as file:
    for line in file.readlines():
        if line.strip() != "":
            input.append(eval(line))

devider_a = [[2]]
devider_b = [[6]]
input.append(devider_a)
input.append(devider_b)

from functools import cmp_to_key
input.sort(key=cmp_to_key(compare), reverse=True)

pos_a = input.index(devider_a) + 1
pos_b = input.index(devider_b) + 1
print(pos_a * pos_b)
