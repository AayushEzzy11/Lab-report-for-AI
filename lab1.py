room_a ="Dirty"
room_b ="Dirty"
location = "Room A"
if location == "Room A":
    print("Vaccum is in Room A")
    if room_a =="Dirty":
        print("Room A is Dirty.Cleaning Room A....")
        room_a = "Clean"
    print("Moving to Room B...")
    location = "Room B"
if location == "Room B":
    print("Vaccum is in Room B..")
    if room_b == "Dirty":
        print("Room B is Dirty.Cleaning Room B ....")
        room_b = "Clean"
print("Room A is ",room_a)
print("Room B is ",room_b)
