rows = []
def test_visibility(rows, x, y):
    visible = False
    number = 1

    v, n = test_to_top(rows, x, y)
    visible = visible or v
    number *= n

    v, n = test_to_bottom(rows, x, y)
    visible = visible or v
    number *= n

    v, n = test_to_left(rows, x, y)
    visible = visible or v
    number *= n

    v, n = test_to_right(rows, x, y)
    visible = visible or v
    number *= n

    return visible, number

def test_to_top(rows, x, y):
    tree = rows[x][y]

    for i in range(x - 1, -1, -1):
        test = rows[i][y]
        if test >= tree:
            return False, x - i
    return True, x

def test_to_bottom(rows, x, y):
    tree = rows[x][y]

    for i in range(x + 1, max_x, 1):
        test = rows[i][y]
        if test >= tree:
            return False, i - x
    return True, max_x - x - 1


def test_to_left(rows, x, y):
    tree = rows[x][y]

    for i in range(y - 1, -1, -1):
        test = rows[x][i]
        if test >= tree:
            return False, y - i
    return True, y

def test_to_right(rows, x, y):
    tree = rows[x][y]

    for i in range(y + 1, max_y, 1):
        test = rows[x][i]
        if test >= tree:
            return False, i - y
    return True, max_y - y - 1

sum = 0
with open('day08/input.txt') as file:
    seed = True
    for row in file.readlines():
        
        column = []
        for tree in row.strip():
            column.append(int(tree))
        rows.append(column)

max_x = len(rows)
max_y = len(rows[0])
max_view = 0

for x in range(max_x):
    for y in range(max_y):
        
        v, n = test_visibility(rows, x, y)
        if v:
            sum += 1
        if max_view < n:
            max_view = n
print(sum)
print(max_view)
