import time

start_time = time.perf_counter()
file = open("input.txt", "r")
lines = file.readlines()

pipes = {'S':['up','down','left','right'],'|':['up','down'],'L':['up', 'right'],'J':['up', 'left'],'7':['down', 'left'],'F':['down', 'right'],'-':['left', 'right'],'.':[]}

def has_neighbours(pos):
    #print(f'Searching neighbours for {pos}')
    x, y = pos
    buf = []
    a_pos, b_pos, c_pos, d_pos = [x-1,y],[x+1,y],[x,y-1],[x,y+1]
    a,b,c,d = 4*['.']#arr[y][x-1],arr[y][x+1],arr[y-1][x],arr[y+1][x]
    if x-1 >= 0:
        a = arr[y][x-1]
    if x+1 < len(arr[0]):
        b = arr[y][x+1]
    if y-1 >= 0:
        c = arr[y-1][x]
    if y+1 < len(arr):
        d = arr[y+1][x]
    pipe = pipes[arr[y][x]]
    #print(a,b,c,d)
    if not a_pos in used and 'left' in pipe and 'right' in pipes[a]:
        buf.append(a_pos)
        used.append(a_pos)
    if not b_pos in used and 'right' in pipe and 'left' in pipes[b]:
        buf.append(b_pos)
        used.append(b_pos)
    if not c_pos in used and 'up' in pipe and 'down' in pipes[c]:
        buf.append(c_pos)
        used.append(c_pos)
    if not d_pos in used and 'down' in pipe and 'up' in pipes[d]:
        buf.append(d_pos)
        used.append(d_pos)
    #print(f'Found {buf}')
    return buf

start = []
arr = []
used = []
for  idx,line in enumerate(lines):
    if 'S' in line:
        start = [line.index('S'), idx]
    arr.append(line.strip('\n'))

ans = 0
neighbours = [has_neighbours(start)]
while True:
    #print(f'# {ans}')
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
