import os
import time

directory = input("Number of problem folder: ")
path = f"{directory}_day"

start_time = time.perf_counter()

try:
    # Create folder
    os.mkdir(path)
    print(f"Created folder {directory}_day")

    # Create file input.txt
    open(f"{path}\\input.txt", "w")
    print(f"Created input.txt")

    # Create file main.py
    with open(f"{path}\\1_part.py", "w") as file:
        file.write(
            f"""import time

start_time = time.perf_counter()
file = open("input.txt", "r")
lines = file.readlines()

for line in lines:
    line = list(map(int, line.split(" ")))
    print(line)

print(f"Part1 done in """
            + "{(time.perf_counter()-start_time):02f}"
            + """ seconds")
"""
        )
    print(f"Created 1_part")
    with open(f"{path}\\2_part.py", "w") as file:
        file.write(
            f"""import time

start_time = time.perf_counter()
file = open("input.txt", "r")
lines = file.readlines()

for line in lines:
    line = list(map(int, line.split(" ")))
    print(line)

print(f"Part2 done in """
            + "{(time.perf_counter()-start_time):02f}"
            + """ seconds")
"""
        )
    print(f"Created 2_part")

    print(f"All done in {(time.perf_counter()-start_time):02f} seconds")
except OSError as error:
    print(error)
