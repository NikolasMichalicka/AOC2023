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

def converter(input_list, output_list):
    for elements in input_list:
        if type(elements) == list:
            converter(elements,output_list)
        else:
            output_list.append(elements)
    return output_list

def convertSeed(interval, seed_map):
    if interval[0] == interval[1]:
        return
    seed = interval[0]
    for x in seed_map:
        if seed >= x[1] and seed < x[1]+x[2]:
            seed += x[0]-x[1]
            seed1 = min(x[1]+x[2]-1,interval[1]) + x[0]-x[1]
            interval = (min(x[1]+x[2],interval[1]),interval[1])
            return [[seed,seed1], convertSeed(interval, seed_map)]
    return [interval[0], interval[1]]


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

intervals = []
for i in range(0,len(seeds),2):
    intervals.append((seeds[i],seeds[i]+seeds[i+1]-1))

for seed_map in [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]:
    new_intervals = []
    #print(intervals)
    while any(intervals):
        interval = intervals[0]
        L = list(convertSeed(intervals[0], seed_to_soil))
        #L = converter(L)
        #print(L)
        if type(L[0]) != list:
            L = [[L[0],L[1]]]
        L = converter(L, [])
        #print(L)
        for i in range(0,len(L)-1,2):
            new_intervals.append((L[i],L[i+1]))
    
        intervals.pop(0)
    for x in new_intervals:
        intervals.append(x)
for x in intervals:
    if answer == None or answer > x[0]:
        answer = x[0]

print(answer)
