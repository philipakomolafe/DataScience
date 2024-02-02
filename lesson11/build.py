# lets build fun stuff According to the neato's of python.
# lets say we wanna build a game that walk you through an architectural layout 😅😁
# lets get coding!!!!!

# from random import choice, randint

# # here python represents your tour-guide.
# python = choice("123456")

# # And of-course the user is the player 😁..
# user = input("Select Either of Any..\n1- Door in Front\n2- Open Door\n3- Move Forward\n4- Turn Left\n5- Climb Stairs\n6- Move Barkward\n\n")

# # NOTE POSSIBILITY of USER entering WRONG INPUTS
# usr_chose = int(user)
# print(f"USER CHOSE: {usr_chose}")

# def if_else(integer):

#     if (integer % 2 != 0):
#         return "Weird"
#     elif (integer in range(2, 6)) and (integer % 2 == 0):
#         return "Not Weird"
#     elif (integer in range(6, 21)) and (integer % 2 == 0):
#         return "Weird"
#     elif (integer % 2 == 0) and (integer > 20):
#         return "Not Weird"


# if __name__ == "__main__":
#     n = int(input().strip())

#     result = if_else(n)
#     print(f"Pick 'em ALL: {result}")

if __name__ == "__main__":
    n = int(input("Enter Number within 1-100.."))
    if n in []:
        pass
