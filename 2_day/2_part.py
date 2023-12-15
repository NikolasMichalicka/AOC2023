file = open("input.txt", "r")
lines = file.readlines()

a = 0
for i, line in enumerate(lines):
    line = line.strip("\n").split(":")[1].split(";")
    max = {"red": 0, "green": 0, "blue": 0}
    for x in line:
        for y in x.split(","):
            y = y.strip()
            z = y.split(" ")
            if max[z[1]] < int(z[0]):
                max[z[1]] = int(z[0])
    a += max["red"] * max["green"] * max["blue"]
print(a)
