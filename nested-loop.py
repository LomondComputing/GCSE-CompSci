floors=6
rooms=4
hotelRooms=[[str(row)+str(col) for floor in range(1,floors+1)] for room in range(1,rooms+1)]


# print out a row at a time
for floor in range(floors):    
    print(hotelRooms[floor])
