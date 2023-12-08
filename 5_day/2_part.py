file = open("input.txt", "r")
lines = file.readlines()
lines_lenght = len(lines)

def getMap():
    buf = []
    global index, lines_lenght
    index+=1
    while True:
        index+=1
        if(index == lines_lenght):
            break
        str = lines[index].strip("\n")
        if (str == ""):
            break
        buf.append(list(map(int, str.split())))
    return buf

def convertSeed(seed, seed_map):
    for x in seed_map:
        if seed >= x[1] and seed < x[1]+x[2]:
            seed += x[0]-x[1]
            return seed
    return seed


seeds =  list(map(int, lines[0].split(":")[1].strip(" ").split()))
index = 1
seed_to_soil = getMap()
soil_to_fertilizer = getMap()
fertilizer_to_water = getMap()
water_to_light = getMap()
light_to_temperature = getMap()
temperature_to_humidity = getMap()
humidity_to_location = getMap()
answer = None

for i in range(0,len(seeds),2):
    for j in range(seeds[i+1]):
        seed = seeds[i]+j
        seed = convertSeed(seed, seed_to_soil)
        seed = convertSeed(seed, soil_to_fertilizer)
        seed = convertSeed(seed, fertilizer_to_water)
        seed = convertSeed(seed, water_to_light)
        seed = convertSeed(seed, light_to_temperature)
        seed = convertSeed(seed, temperature_to_humidity)
        seed = convertSeed(seed, humidity_to_location)
        if answer == None or seed < answer:
            answer = seed

print(answer)
