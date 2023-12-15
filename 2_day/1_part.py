file = open("input.txt", "r")
lines = file.readlines()

a = 0
for i, line in enumerate(lines):
    line = line.strip("\n").split(":")[1].split(";")
    possible = True
    for x in line:
        sum = {"red": 0, "green": 0, "blue": 0}
        for y in x.split(","):
            y = y.strip()
            z = y.split(" ")
            sum[z[1]] += int(z[0])
        if sum["red"] > 12 or sum["green"] > 13 or sum["blue"] > 14:
            possible = False
    if possible:
        a += i + 1
print(a)
