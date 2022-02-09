import random
roomsAssigned=[1]
room_numbers = 1
groupList=["Ropes", "Rafting", "Obtacle", "Wellness"]
count=0
print("Welcom to CompanyPro's Team-Buikding Weekend!")
name=input("Please enter your name (q to quit)? ")
while name != 'q' and count < 50:
    while room_numbers in roomsAssigned:
        room_numbers= random.randint(1,50)
    print(f"{name}, your room number is {room_numbers}")
    roomsAssigned.append(room_numbers)
    group = random.choice(groupList) 
    print(f"You will meet with the {group} Group this afternoon.")
    count+=1
    name=input("Please enter your name (q to quit)? ")