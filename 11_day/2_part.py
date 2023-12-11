import time

start_time = time.perf_counter()
file = open("input.txt", "r")
lines = file.readlines()

for line in lines:
    line = list(map(int, line.split(" ")))
    print(line)

print(f"Part2 done in {(time.perf_counter()-start_time):02f} seconds")
