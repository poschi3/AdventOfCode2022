import copy

current_dir = []
files = dict()
dirs = dict()
dirs["/"] = 0

def command_cd(command, current_dir):
    if command[2] == "/":
        current_dir = []
    elif command[2] == "..":
        current_dir.pop()
    else:
        current_dir.append(command[2])

def not_end_of_ls(lines):
    if len(lines) <= 0:
        return False
    if len(lines[0]) <= 0:
        return False
    if lines[0][0] == "$":
        return False
    return True

def get_path(current_dir, name):
    path = "/".join(current_dir)
    if not name is None:
        path += "/" + name
    if len(path) > 0 and path[0] != "/":
        path = "/" + path
    return path

def command_ls(lines):
    while not_end_of_ls(lines):
        info = lines.pop(0).strip().split(" ")
        if info[0] != "dir":
            filename = get_path(current_dir, info[1])
            size = int(info[0])
            files[filename] = size

            my_dir = copy.deepcopy(current_dir)
            while len(my_dir) > 0:
                dirpath = get_path(my_dir, None)
                if not dirpath in dirs:
                    dirs[dirpath] = 0
                dirs[dirpath] += size
                my_dir.pop(-1)
            dirs["/"] += size

with open('day07/input.txt') as file:
    lines = file.readlines()
    while len(lines) > 0:
        command = lines.pop(0).strip().split(" ")
        
        if command[1] == "cd":
            command_cd(command, current_dir)
        elif command[1] == "ls":
            command_ls(lines)
        else:
            raise ValueError("Unknown command " + command[1])

sum_sub = 0
count = 0
for dir in dirs:
    dirsize = dirs[dir]
    if dir != "" and dirsize < 100000:
        sum_sub += dirsize
print(sum_sub)


free = 70000000 - dirs["/"]
best_free = 999999999999999999999
best_to_delte = ""
for dir in dirs:
    dirsize = dirs[dir]
    new_free = free + dirsize
    if new_free  >= 30000000:
        if new_free < best_free:
            best_to_delte = dir
            best_free = new_free
print(dirs[best_to_delte])
