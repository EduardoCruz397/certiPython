grade = 76
rank = 3

if grade > 80 and rank >= 3:
    grade +=10
elif grade >= 70 and rank > 3:
    grade += 5
else:
    grade -= 5

print(grade)