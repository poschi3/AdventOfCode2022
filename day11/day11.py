import copy

class Monkey:
    inspections = 0
    def __init__(self, instructions: str):

        lines = instructions.split("\n")
        start_items = lines[1].strip().split(":")
        self.items = [int(x.strip()) for x in start_items[1].strip().split(",")]

        self.calc = self.prepare_calc(lines[2].split(" ")[-2:])
        self.divisible_by = int(lines[3].split(" ")[-1])
        self.test_true = int(lines[4].split(" ")[-1])
        self.test_false = int(lines[5].split(" ")[-1])

    def prepare_calc(self, operation):
        if operation[0] == "*":
            opx = lambda x, y: x * y
        elif operation[0] == "+":
            opx = lambda x, y: x + y

        if operation[1] == "old":
            return lambda x: opx(x, x)
        else:
            value = int(operation[1])
            return lambda x: opx(x, value)

    def do(self, other_monkeys, boring_devisor, devisor):
        while len(self.items) > 0:
            self.inspections += 1
            worry_level = self.items.pop(0)
            worry_level = self.calc(worry_level)
            worry_level = worry_level // boring_devisor
            worry_level = worry_level - ((worry_level // devisor) * devisor)

            if worry_level % self.divisible_by == 0:
                other_monkeys[self.test_true].items.append(worry_level)
            else:
                other_monkeys[self.test_false].items.append(worry_level)

def heavy_workers(monkeys):
    instructions = 1
    for monkey in monkeys[:2]:
        instructions *= monkey.inspections
    return instructions


monkeys_a = []
devisor = 1
with open('day11/input.txt') as file:
    for raw_monkey in file.read().split("\n\n"):
        m = Monkey(raw_monkey)
        devisor *= m.divisible_by
        monkeys_a.append(m)
monkeys_b = copy.deepcopy(monkeys_a)


for _ in range(20):
    for monkey in monkeys_a:
        monkey.do(monkeys_a, 3, devisor)
monkeys_a.sort(key=lambda x: x.inspections, reverse=True)
print(heavy_workers(monkeys_a))


for _ in range(10000):
    for monkey in monkeys_b:
        monkey.do(monkeys_b, 1, devisor)
monkeys_b.sort(key=lambda x: x.inspections, reverse=True)
print(heavy_workers(monkeys_b))
