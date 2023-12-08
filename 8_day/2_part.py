import time

start_time = time.perf_counter()
file = open("input.txt", "r")
lines = file.readlines()

nodes = {}
moves = lines[0].strip(" ")
starts = []
for line in lines[2:]:
    name = line.split()[0]
    if name[2] == 'A':
        starts.append(name)
    left, right = line[7:15].strip("\n").split(", ")
    nodes[name] = {"L":left,"R":right}

steps = []
for start in starts:
    move = start
    i = 0
    step = 0
    while True:
        step += 1
        move = nodes[move][moves[i]]
        if move[2] == 'Z':
            break

        i += 1
        if i==len(moves)-1:
            i = 0
    steps.append(step)

def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)
 
def LcmOfArray(arr, idx=0):
    if (idx == len(arr)-1):
        return arr[idx]
    a = arr[idx]
    b = LcmOfArray(arr, idx+1)
    return int(a*b/gcd(a,b))

print(LcmOfArray(steps))
print(f"Part1 done in {(time.perf_counter()-start_time):02f} seconds")
