import time

start_time = time.perf_counter()
file = open("input.txt", "r")
lines = file.readlines()

nodes = {}
moves = lines[0].strip(" ")
for line in lines[2:]:
    name = line.split()[0]
    left, right = line[7:15].strip("\n").split(", ")
    nodes[name] = {"L":left,"R":right}

move = 'AAA'
i = 0
steps = 0
while True:
    steps += 1
    move = nodes[move][moves[i]]
    if move == 'ZZZ':
        break

    i += 1
    if i==len(moves)-1:
        i = 0
        
print(steps)
print(f"Part1 done in {(time.perf_counter()-start_time):02f} seconds")