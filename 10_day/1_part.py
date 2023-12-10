import time

start_time = time.perf_counter()
file = open("input.txt", "r")
lines = file.readlines()

pipes = ['|','L','J','7','F','-']

def has_pipes(pipe):
    if pipe == '|':
        return []


def has_neighbours(pos):
    print(f'Searching neighbours for {pos}')
    x, y = pos
    buf = []
    a_pos, b_pos, c_pos, d_pos = [x-1,y],[x+1,y],[x,y-1],[x,y+1]
    a,b,c,d = arr[y][x-1],arr[y][x+1],arr[y-1][x],arr[y+1][x]
    print(a,b,c,d)
    if not a_pos in used and a in pipes and a_pos[0]>=0:
        buf.append(a_pos)
        used.append(a_pos)
    if not b_pos in used and b in pipes and b_pos[0]<=len(arr[0])-1:
        buf.append(b_pos)
        used.append(b_pos)
    if not c_pos in used and c in pipes and c_pos[1]>=0:
        buf.append(c_pos)
        used.append(c_pos)
    if not d_pos in used and d in pipes and d_pos[1]<=len(arr)-1:
        buf.append(d_pos)
        used.append(d_pos)
    print(f'Found {buf}')
    return buf

start = []
arr = []
used = []
for  idx,line in enumerate(lines):
    if 'S' in line:
        start = [line.index('S'), idx]
    arr.append(line.strip('\n'))

print(start)
ans = 0
neighbours = [has_neighbours(start)]
while True:
    neighbours_new = []
    for neighbour in neighbours:
        for neigh in neighbour:
            neighbours_new.append(has_neighbours(neigh))
    if neighbours_new == []:
        break
    neighbours = neighbours_new
    ans += 1
print(ans)
print(f"Part1 done in {(time.perf_counter()-start_time):02f} seconds")
