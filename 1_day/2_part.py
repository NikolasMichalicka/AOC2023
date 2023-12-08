file = open("input.txt", "r")
lines = file.readlines()
digits = "0123456789"
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0

for line in lines:
    line = line.strip("\n")
    print(line)
    first, last = 0, 0
    for i in range(len(line)):
        x = line[i : i + 5]
        if x[0] in digits:
            first = int(x[0])
            break
        if x[1] in digits:
            first = int(x[1])
            break
        for j in range(len(numbers)):
            if numbers[j] in x:
                first = j + 1
                break
        if first != 0:
            break

    line = line[::-1]
    for i in range(len(line)):
        x = line[i : i + 5]
        if x[0] in digits:
            last = int(x[0])
            break
        if x[1] in digits:
            last = int(x[1])
            break
        for j in range(len(numbers)):
            if numbers[j][::-1] in x:
                last = j + 1
                break
        if last != 0:
            break

    sum += int(f"{first}{last}")
    # print(first, last, sum)
    # input()
print(sum)
