file = open("input.txt", "r")
lines = file.readlines()
digits = "0123456789"
sum = 0

for line in lines:
    line = line.strip("\n")
    first, last = 0, 0
    for char in line:
        if char in digits:
            first = int(char)
            break
    for char in reversed(line):
        if char in digits:
            last = int(char)
            break
    sum += int(f"{first}{last}")
print(sum)
