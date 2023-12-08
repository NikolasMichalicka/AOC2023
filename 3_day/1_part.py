file = open("input.txt", "r")
lines = file.readlines()

nums = "0123456789"
symbols = ["*", "@", "#", "$", "+", "%", "/", "&", "=", "-"]


def isPart(x, y):
    for a in x:
        left = a > 0
        right = a < len(lines[0].strip("\n")) - 1
        up = y > 0
        down = y < len(lines) - 1

        if up:
            if lines[y - 1][a] in symbols:
                return True
        if down:
            if lines[y + 1][a] in symbols:
                return True
        if left:
            if lines[y][a - 1] in symbols:
                return True
        if right:
            if lines[y][a + 1] in symbols:
                return True
        if up and left:
            if lines[y - 1][a - 1] in symbols:
                return True
        if up and right:
            if lines[y - 1][a + 1] in symbols:
                return True
        if down and left:
            if lines[y + 1][a - 1] in symbols:
                return True
        if down and right:
            if lines[y + 1][a + 1] in symbols:
                return True

    return False


sum = 0
for y in range(len(lines)):
    line = lines[y].strip("\n")
    # print(line)
    skipx = 0
    for x in range(len(line)):
        if x < skipx:
            continue

        number = 0
        xs = []
        if line[x] in nums:
            number = int(line[x])
            bufferX = x
            xs.append(x)
            while True:
                bufferX += 1
                if bufferX == len(line) or line[bufferX] not in nums:
                    break
                number = int(f"{number}{line[bufferX]}")
                xs.append(bufferX)

            if isPart(xs, y):
                skipx = xs[-1] + 1
                print(number, x)
                sum += number
print(sum)
