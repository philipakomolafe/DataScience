#welcome

users = ["philly", "sue", "ronke"]

print("ronke".upper() in users)
print(users.index("ronke"))

# append item
users.append("mike")
print(users)

users.extend(["Jimmy", "malon", "julie"])
print(users)

users += ["buggie"]
print(len(users))

# insert item
users.insert(0, "banshee")
print(len(users))
print(users)

# remove item
users.remove("banshee")
print(users)

# delete items  
del users[2]
print(users)

users.sort()
print(users)

users.append("daeken")
# users.sort(key=str.capitalize)
# print(users)

print(sorted(users, reverse = True))
print(users)

# list copy
mylist = users[:]
nlist = users.copy()
myuser = list(users)

print(myuser)

mytuple = tuple((1,3,4,"APPLE", 4,8,9,3,2,2,2))
print(mytuple)
print(type(mytuple))

# create list from tuples
newList = list(mytuple)

print(newList)

one, two, *three = newList
print(one)
print(two)
print(three)

print(mytuple.count("apple".upper()))
print(mytuple.count(2))