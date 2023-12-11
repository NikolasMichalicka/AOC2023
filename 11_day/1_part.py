import time

start_time = time.perf_counter()
file = open("input.txt", "r")
lines = file.readlines()

def rotate(arr):
    new_arr = []
    for i in range(len(arr[0])):
        line = ''
        for j in range(len(arr)):
            line+=arr[j][i]
        new_arr.append(line)
    return new_arr


universe = []


for line in lines:
    line = line.strip('\n')
    universe.append(line)
    if '#' not in line:
        universe.append(line)    

universe = rotate(universe)
new_univ = []
for line in universe:
    new_univ.append(line)
    if '#' not in line:
        new_univ.append(line)

galaxies = []
universe = rotate(new_univ)
for y, line in enumerate(universe):
    print(line)
    line = list(line)
    while '#' in line:
        x = line.index('#')
        galaxies.append([x,y])
        line.pop(x)
ans = 0
print(galaxies)
for i in range(len(galaxies)):
    #print(f'i:{i}{galaxies[i]}')
    galaxy = galaxies[i]
    #print(f'next galaxy:{galaxy}')
    for x in galaxies[i+1:]:
        ans+=abs(galaxy[0]-x[0])+abs(galaxy[1]-x[1])
        '''buf = list(x)
        while buf != galaxy:
            #print(f'galaxy1:{galaxy}')
            #print(f'galaxy2:{buf}')
            ans+=1
            difx, dify = galaxy[0]-buf[0], galaxy[1]-buf[1]
            if abs(difx) > abs(dify):
                if(buf[1]==galaxy[1] and buf[0]+int(difx/abs(difx))==galaxy[0]):
                    break
                if universe[buf[1]][buf[0]+int(difx/abs(difx))] == '.':
                    buf[0]+=int(difx/abs(difx))
                elif dify == 0:
                    if buf[1]>0:
                        buf[1]-=1
                    else:
                        buf[1]+=1
                else:
                    buf[1]+=int(dify/abs(dify))
            else:
                if(buf[0]==galaxy[0] and buf[1]+int(dify/abs(dify))==galaxy[1]):
                    break
                if universe[buf[1]+int(dify/abs(dify))][buf[0]] == '.':
                    buf[1]+=int(dify/abs(dify))
                elif difx == 0:
                    if buf[0]>0:
                        buf[0]-=1
                    else:
                        buf[0]+=1
                else:
                    buf[0]+=int(difx/abs(difx))
        '''

print(ans)
print(f"Part1 done in {(time.perf_counter()-start_time):02f} seconds")
