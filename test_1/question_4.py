# NOTE - This question may be a little bit more confusing because the
# test is Java-translated

# Question:

# The class Box has 4 attributes:
# color: String
# length: int
# width: int
# height: int
#
# The class has also a method that gets all it's attributes as params
# and sets the values of the object's attributes.
# 1. write a constructor method that create a black box that all it's dimensions
# (length, width, height) are random numbers between 20 and 100.
# The method title: def __init__(self, color):
# (you can change the method title.)
#
# 2. A "Black White List" called a list of Box objects with at least one white box
# and at least one black box with no boxes in other color.
#
# Write a function that takes a list of Box objects and check if the list is
# a "Black White List".
# The function title: def is_black_white(arr):

import random


# 1.
# NOTE: Wrote the class for test only, the solution is in the "__init__() method".
class Box:
    def set_properties(self, width, height, length, color):
        self.width = width
        self.height = height
        self.length = length
        self.color = color

    def __init__(self, color):
        self.color = "black"
        self.width = random.randint(20, 100)
        self.length = random.randint(20, 100)
        self.height = random.randint(20, 100)


b_box = Box("black")
print(b_box.width, b_box.height, b_box.width, b_box.color)


# 2.
def is_black_white(arr):
    has_black_box = False
    has_white_box = False
    has_another_color = False
    for box in arr:
        if box.color == "black":
            has_black_box = True
        elif box.color == "white":
            has_white_box = True
        else:
            has_another_color = True
    if has_black_box and has_white_box and not has_another_color:
        return True
    else:
        return False


black_box = Box("black")
white_box = Box("black")
white_box.set_properties(40, 40, 40, "white")
print(is_black_white([black_box, white_box]))
red_box = Box("black")
red_box.set_properties(40, 40, 40, "red")
print(is_black_white([black_box, white_box, red_box]))
