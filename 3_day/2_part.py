file = open("input.txt", "r")
lines = file.readlines()

nums = "0123456789"
symbol = "*"


def getNumber(number, x, y):
    bufferX = x - 1
    while bufferX >= 0:
        if lines[y][bufferX] not in nums:
            break
        number = f"{lines[y][bufferX]}{number}"
        bufferX -= 1
    bufferX = x + 1
    while bufferX <= len(lines[0].strip("\n")) - 1:
        if lines[y][bufferX] not in nums:
            break
        number = f"{number}{lines[y][bufferX]}"
        bufferX += 1
    return int(number)


def hasGear(x, y):
    numbers = []
    left = x > 0
    right = x < len(lines[0].strip("\n")) - 1
    up = y > 0
    down = y < len(lines) - 1

    if up:
        if lines[y - 1][x] in nums:
            up = False
            number = int(lines[y - 1][x])
            numbers.append(getNumber(number, x, y - 1))

    if down:
        if lines[y + 1][x] in nums:
            down = False
            number = int(lines[y + 1][x])
            numbers.append(getNumber(number, x, y + 1))
    if left:
        if lines[y][x - 1] in nums:
            left = False
            number = int(lines[y][x - 1])
            numbers.append(getNumber(number, x - 1, y))
    if right:
        if lines[y][x + 1] in nums:
            right = False
            number = int(lines[y][x + 1])
            numbers.append(getNumber(number, x + 1, y))
    if up and left:
        if lines[y - 1][x - 1] in nums:
            number = int(lines[y - 1][x - 1])
            numbers.append(getNumber(number, x - 1, y - 1))
    if up and right:
        if lines[y - 1][x + 1] in nums:
            number = int(lines[y - 1][x + 1])
            numbers.append(getNumber(number, x + 1, y - 1))
    if down and left:
        if lines[y + 1][x - 1] in nums:
            number = int(lines[y + 1][x - 1])
            numbers.append(getNumber(number, x - 1, y + 1))
    if down and right:
        if lines[y + 1][x + 1] in nums:
            number = int(lines[y + 1][x + 1])
            numbers.append(getNumber(number, x + 1, y + 1))
    if len(numbers) == 2:
        return numbers[0] * numbers[1]
    return 0


sum = 0
for y in range(len(lines)):
    line = lines[y].strip("\n")
    for x in range(len(line)):
        if line[x] == symbol:
            sum += hasGear(x, y)

print(sum)
