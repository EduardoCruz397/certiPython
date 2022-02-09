from numpy import average


employee_payn = [15000, 120000, 35000, 45000]
count = 0
sum = 0

for index in range(0, len(employee_payn)):
    print(employee_payn[index])
    count += 1
    sum += employee_payn[index]
average = sum/count
print("The total payroll is: ", sum)
print("teh average salary is: ", average)