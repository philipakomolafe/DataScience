# String Data_type

first = " Philip                 "
last = "Akomolafe"

print(type(first))

print(type(last) == int)
print(type(last) == str)

pizza = str('pepperoni')
print(type(pizza)== str)
print(isinstance(pizza, str))

#casting 
decade = str(1980)
print(type(decade))
print(decade)

#String Methods
print(first)
print(first.lower())
print(first.upper())
print(len(first.strip())) #strip for removing unnecessary spaces 

game = "Tournament".upper()

print(game.center(40, "="))
print("")
print("Chelsea".ljust(20, ".") + "108pt".rjust(10))
print("Manchester".ljust(20, ".") + "100pt".rjust(10))
print("Gibona FC".ljust(20, ".") + "400pt".rjust(10))


gpa = float(4.056)
print(abs(gpa))
print(round(gpa))


import math

print(round(math.pi))
print(math.ceil(gpa))