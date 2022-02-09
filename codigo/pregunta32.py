name = input("Enter your name: ")

if name.lower() == name:
    print(name, "is all lower case")
elif name.upper() == name:
    print(name, "is all upper case")
else:
    print("is Mixed case")