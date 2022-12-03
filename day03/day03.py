from typing import List

def contains(item, packages: List[str]):
    for package in packages:
        if not package.__contains__(item):
            return False
    return True

def find_shared(packages: List[str]):
    assert len(packages) >= 2, "Must be 2 or more packages"
    for item in packages[0]:
        if contains(item, packages[1:]):
            return item

def get_priority(item: str):
    if(item >= "a" and item <= "z"):
        return ord(item) - 96
    if (item >= "A" and item <= "Z"):
        return ord(item) - 38
    else:
        assert False, "Unknown item"

priorities_part_1 = 0
priorities_part_2 = 0
with open('input.txt') as file:
    group = []
    for rucksack in file.readlines():
        rucksack = rucksack.strip()

        # Part 1
        first = rucksack[:int(len(rucksack)/2)]
        second = rucksack[-int(len(rucksack)/2):]
        shared = find_shared([first, second])
        priorities_part_1 += get_priority(shared)

        # Part 2
        group.append(rucksack)

        if len(group) >= 3:
            shared = find_shared(group)
            priorities_part_2 += get_priority(shared)
            group = []

print(priorities_part_1)
print(priorities_part_2)
