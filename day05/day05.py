import copy

stacks_a = dict()
stacks_b = dict()
with open('day05/input.txt') as file:
    seed = True
    for line in file.readlines():
        if line.startswith(" 1") or line == "\n":
            seed = False
            stacks_b = copy.deepcopy(stacks_a)
            continue
        if seed:
            for n in range(int(len(line)/4)):
                element = line[n*4+1:n*4+2]
                elementNo = str(n+1)
                if not elementNo in stacks_a:
                    stacks_a[elementNo] = []
                
                if not element == " ":
                    stacks_a[elementNo].append(element)
        else:
            # Part A
            moves = [x.strip() for  x in line.split(" ")]
            for n in range(int(moves[1])):
                element = stacks_a[moves[3]].pop(0)
                stacks_a[moves[5]].insert(0, element)

            # Part B
            elements = []
            for n in range(int(moves[1])):
                elements.append(stacks_b[moves[3]].pop(0))
            elements.reverse()
            for element in elements:
                stacks_b[moves[5]].insert(0, element)

result_a = ""
for s in range(1, len(stacks_a)+1):
    result_a += stacks_a[str(s)][0]
print(result_a)

result_b = ""
for s in range(1, len(stacks_b)+1):
    result_b += stacks_b[str(s)][0]
print(result_b)
