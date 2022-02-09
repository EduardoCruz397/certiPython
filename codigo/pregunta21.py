salary_list =  [22,150000,32]

for index in range(len(salary_list)):    
    if salary_list[index] >=150000:
        continue
    salary_list[index] =(salary_list[index] * 1.3) + 500
    print(salary_list[index])