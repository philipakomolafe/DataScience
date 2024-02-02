# intro to recursion - this gives the possibility of re-calling your code.

import os


def file_traversal(path):
    for item in os.listdir(path):

        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            print(full_path)
        else:
            file_traversal(full_path)


def generate_range(start, end):
    if (start > end):
        return 0
    else:
        print(start)
        generate_range(start + 1, end)


val1 = generate_range(2, 20)
print(val1)

val2 = file_traversal("C:/Users/USER/Desktop/Code/DataScience/.vscode")
print(val2)
