floors=6
rooms=4

hotelRooms=[[str(floor)+str(room) for room in range(1,rooms+1)] for floor in range(1,floors+1)]

for floor in range(floors-1,-1,-1):    
    print(hotelRooms[floor])
