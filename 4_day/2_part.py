import time

start_time = time.perf_counter()
file = open("input.txt", "r")
lines = file.readlines()


def getMatches(line):
    buf = 0
    line = line.strip("\n").replace("  ", " ").split(":")[1].strip().split(" | ")
    winning = list(map(int, line[0].split()))
    nums = list(map(int, line[1].split()))
    for num in nums:
        if num in winning:
            buf += 1
    return buf


copies = [1] * len(lines)
points = 0
for i in range(len(lines)):
    for a in range(copies[i]):
        points += 1
        buf = getMatches(lines[i])
        for j in range(buf):
            copies[i + 1 + j] += 1
print(points)
print(f"Part2 done in {(time.perf_counter()-start_time):02f} seconds")
