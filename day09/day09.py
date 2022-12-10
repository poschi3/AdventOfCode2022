
class Part:
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y

    def right(self):
        self.x += 1

    def left(self):
        self.x -= 1

    def up(self):
        self.y += 1

    def down(self):
        self.y -= 1

    def touches(self, other):
        return (
            self.x <= other.x + 1 and
            self.x >= other.x - 1 and
            self.y <= other.y + 1 and
            self.y >= other.y - 1)

    def follow(self, head):
        if not self.touches(head):
            if head.x > self.x:
                self.x += 1
            elif head.x < self.x:
                self.x -= 1

            if head.y > self.y:
                self.y += 1
            elif head.y < self.y:
                self.y -= 1

def snake(snake):
    touched = set()

    with open('day09/input.txt') as file:
        for command in file.readlines():
            command = command.strip().split(" ")

            direction = command[0]
            steps = int(command[1])

            for x in range(0, steps):
                H = snake[0]
                if direction == "R":
                    H.right()
                elif direction == "L":
                    H.left()
                elif direction == "U":
                    H.up()
                elif direction == "D":
                    H.down()

                last_p = H
                for P in snake[1:]:
                    P.follow(last_p)
                    last_p = P

                T = snake[-1]
                touched.add((T.x, T.y))

    print(len(touched))

snake_1 = [Part(), Part()]
snake(snake_1)

snake_2 = [Part(), Part(), Part(), Part(), Part(), Part(), Part(), Part(), Part(), Part()]
snake(snake_2)
