class CPU:
    special_cycles = (20, 60, 100, 140, 180, 220)
    crt_lenght = 40

    x = 1
    cycle = 0
    sum = 0

    def noop(self):
        self.draw()
        self.do_cycle()

    def addx(self, value):
        self.noop()
        self.draw()
        self.do_cycle()
        self.x += int(value)

    def do_cycle(self):
        self.cycle += 1
        if self.cycle in self.special_cycles:
            self.sum += self.cycle * self.x
    def draw(self):
        if self.cycle % 40 == 0:
            print()
        if self.cycle %40 >= (self.x-1) and self.cycle %40 <= (self.x+1):
            print("#", end="")
        else:
            print(".", end="")

cpu = CPU()
with open('day10/input.txt') as file:
    for command in file.readlines():
        split = command.strip().split(" ")

        if split[0] == "noop":
            cpu.noop()
        elif split[0] == "addx":
            cpu.addx(split[1])
        else:
            raise ValueError("Unknown inst " + split[0])
print()
print(cpu.sum)
