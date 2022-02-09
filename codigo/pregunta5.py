from turtle import distance


def get_name():
    name = input("Whats is your name? ")
    return name
def calc_calories(miles, calorias_per_mile):
    calories = miles * calorias_per_mile
    return calories
distance = int(input("How many did you bike this wek? "))
burn_rate = 50
biker= get_name()
calories_burned = calc_calories(distance, burn_rate)
print(biker, ", you burned about ", calories_burned, " calories.")