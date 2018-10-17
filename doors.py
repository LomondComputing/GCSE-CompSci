
doors = [ False for i in range(100) ]

for door in range(len(doors)):
    for i in range(len(doors),door):
        doors[i] = not doors[i]

for door in range(len(doors)):
    if doors[door]:
        print(door+1)

