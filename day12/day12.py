def find_arround(heights, pos):
    x, y = pos
    funcs = [
        lambda x, y: (x-1, y),
        lambda x, y: (x+1, y),
        lambda x, y: (x, y-1),
        lambda x, y: (x, y+1)
    ]

    found = []
    for func in funcs:
        test_pos = func(x, y)
        if(test_pos in heights):
            if heights[test_pos] <= heights[pos] + 1:
                found.append(test_pos)

    return found

with open('day12/input.txt') as file:
    input = [x.strip() for x in file.readlines()]

heights = dict()

open_list_a = dict()
open_list_b = dict()

for x in range(0, len(input)):
    for y in range(0, len(input[x])):

        char = input[x][y]
        if char == "S":
            heights[(x, y)] = 0
            open_list_a[(x, y)] = 0
            open_list_b[(x, y)] = 0
        elif char == "E":
            heights[(x, y)] = 25
            end = (x, y)
        else:
            height = ord(char) - 97
            heights[(x, y)] = height
            if char == "a":
                open_list_b[(x, y)] = 0

def route(open_list):
    closed_list = dict()
    while len(open_list) > 0:
        sorted_open_list = sorted(open_list.items(), key=lambda item: item[1])

        key, value = list(sorted_open_list)[0]
        if key == end:
            return str(value)
        del open_list[key]
        
        for new_pos in find_arround(heights, key):
            if(not new_pos in closed_list):
                open_list[new_pos] = value + 1
        closed_list[key] = value

# Part A:
print(route(open_list_a))
print(route(open_list_b)) # Correct on test, off by one on real input
