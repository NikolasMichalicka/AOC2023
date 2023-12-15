import time

start_time = time.perf_counter()
file = open("input.txt", "r")
lines = file.readlines()

universe = [[x for x in line.strip('\n')]for line in lines]

y_empty = []
for i, line in enumerate(universe):
    if '#' not in line:
        y_empty.append(i)

x_empty = []
for i in range(len(universe[0])):
    line = [x[i] for x in universe]
    if '#' not in line:
        x_empty.append(i)

galaxies = []
for y in range(len(universe)):
    for x in range(len(universe[0])):
        if universe[y][x] == '#':
            galaxies.append((x,y))

ans = 0
for i, (x,y) in enumerate(galaxies):
    for (x2,y2) in galaxies[i+1:]:
        dis = abs(x-x2) + abs(y-y2)
        for ex in x_empty:
            if min(x,x2)<= ex <=max(x,x2):
                dis+=1_000_000-1
        for ey in y_empty:
            if min(y,y2)<= ey <= max(y,y2):
                dis+=1_000_000-1
        ans+=dis

print(ans)
print(f"Part2 done in {(time.perf_counter()-start_time):02f} seconds")
