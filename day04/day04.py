def contains(section_1: set, section_2: set) -> bool:
    if section_1.issubset(section_2):
        return True
    if section_2.issubset(section_1):
        return True
    return False

count_a = 0
count_b = 0
with open('day04/input.txt') as file:
    for plan in file.readlines():
        s1, s2 = plan.strip().split(",")
        s1_start, s1_stop = [int(x) for x in s1.split("-")]
        s2_start, s2_stop = [int(x) for x in s2.split("-")]

        section_1 = set(range(s1_start, s1_stop + 1))
        section_2 = set(range(s2_start, s2_stop + 1))
        
        if contains(section_1, section_2):
            count_a += 1

        if not section_1.isdisjoint(section_2):
            count_b += 1

print(count_a)
print(count_b)
