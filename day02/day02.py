# Elf: A Rock/Stein, B Paper/Papier, C Scissors/Schere
# Me: X Rock/Stein +1, Y Paper/Papier +2, Z Scissors/Schere +3
# lose +0, draw +3, win +6

choose_score = { "X": 1, "Y": 2, "Z": 3 }
win_combinations = { "A": "Y", "B": "Z", "C": "X" }
draw_combinations = { "A": "X", "B": "Y", "C": "Z" }
lose_combinations = { "A": "Z", "B": "X", "C": "Y" }

# Part 2: X lose, Y draw, Z win
combinator = { "X": lose_combinations, "Y": draw_combinations, "Z": win_combinations }

def calc_score(elf, me):
    score = 0
    score += choose_score[me]
    if draw_combinations[elf] is me:
        score += 3
    elif win_combinations[elf] is me:
        score += 6
    # else loss, no score
    return score

part_one_score = 0
part_two_score = 0
with open('input.txt') as file:
    currentMax = 0
    for round in file.readlines():
        elf, me = [t.strip() for t in round.split(" ")]
        # Part 1
        part_one_score += calc_score(elf, me)

        # Part 2
        new_me = combinator[me][elf]
        part_two_score += calc_score(elf, new_me)

print(part_one_score)
print(part_two_score)
