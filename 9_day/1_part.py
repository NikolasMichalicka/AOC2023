import time

start_time = time.perf_counter()
file = open("input.txt", "r")
lines = file.readlines()

ans = 0
for index, line in enumerate(lines):
    line = list(map(int, line.split(" ")))
    arrs = [line]
    print(f'({index+1}/{len(lines)})')
    print(line)
    while True:
        arr = []
        last = arrs[-1]
        for i in range(len(last)-1):
            arr.append(last[i+1]-last[i])
        if all(v == 0 for v in arr):
            break
        arrs.append(arr)
        xs = line
        print(arr)
    num = 0
    for arr in arrs:
        num += arr[-1]
    print(num)
    ans+=num

print(ans)
print(f"Part1 done in {(time.perf_counter()-start_time):02f} seconds")
