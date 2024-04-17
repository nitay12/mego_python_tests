# V1 - with "in" usage
string = input("enter a string: ")
counter = 0
while "Z" not in string:
    if string[0] == "X" and string[-1] == "X":
        counter += 1
    string = input("enter a string: ")
print(counter)

# V2 - without "in" usage
string = input("enter a string: ")
counter = 0
contains_Z = False
while not contains_Z:
    for char in string:
        if char == "Z":
            contains_Z = True
    if contains_Z:
        break
    if string[0] == "X" and string[-1] == "X":
        counter += 1
    string = input("enter a string: ")
print(counter)