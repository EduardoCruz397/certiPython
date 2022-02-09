from email import message


age = input("Cual es tu edad? ")
year = input("Ingresa el año actual ")
born = eval(year) - eval(age)
message = "Ty año de nacimiento es " + str(born)

print(message)
print(type(age))
print(type(born))
print(type(message))
