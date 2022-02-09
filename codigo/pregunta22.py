def admission_fee(age, school):
    rate = 0
    if age >= 5 and school == True:
        rate = 10
    elif age <=17 and school == False:
        rate = 20
    else:
        rate = 50
    return rate

print(admission_fee(18, True))