from random import randint
target = randint(1,10)

chance = 1
print("Guss an integer from 1 to 10. You will have 3 chances.")

while chance <=3:
    print(chance)
    print(target)
    guess = int(input("Guess an integer: "))
    if guess > target:
        print("Guess is too high")
    elif guess < target:
        print("Guess is too low")
    else:
        print("Guess is just right!")
        break
    chance += 1