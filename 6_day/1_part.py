import time

start_time = time.perf_counter()
file = open("input.txt", "r")
lines = file.readlines()

Time = lines[0].split(":")[1]
Distance = lines[1].split(":")[1]
Time = list(map(int, Time.split()))
Distance = list(map(int, Distance.split()))
ans = 1

for i in range(len(Time)):
    t, d = Time[i], Distance[i]
    start, end = 0, 0
    buf = 0
    while start == 0:
        buf += 1
        if buf*(t-buf) > d:
            start = buf
    
    buf = d
    while end == 0:
        buf -= 1
        if buf*(t-buf) > d:
            end = buf
    ans *= (end-start+1)

print(ans)
print(f"Part1 done in {(time.perf_counter()-start_time):02f} seconds")
