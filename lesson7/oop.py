# intro to classes

class countClick():
    """
    This Class counts the Number of datascientists in attendance.
    """

    def __init__(self, count=0):
        self.count = count

    def username(self, name):
        self.user = name
        print(f"Name: {(self.user).title()}")


user = countClick()
user.username("bayo ")
