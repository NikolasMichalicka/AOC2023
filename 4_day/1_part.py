import time

start_time = time.perf_counter()
file = open("input.txt", "r")
lines = file.readlines()

points = 0
for line in lines:
    buf = 0
    line = line.strip("\n").replace("  ", " ").split(":")[1].strip().split(" | ")
    winning = list(map(int, line[0].split()))
    nums = list(map(int, line[1].split()))
    for num in nums:
        if num in winning:
            if buf == 0:
                buf = 1
            else:
                buf *= 2
    points += buf
print(points)
print(f"Part1 done in {(time.perf_counter()-start_time):02f} seconds")
