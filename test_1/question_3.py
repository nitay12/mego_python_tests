# A whole numbers list called a "Friends List" if every item in the list is
# exist exactly 2 times in the list.
# 1. Write a function that gets a whole numbers list and checks if it is
# a "Friends List". If it is a "Friends List" the function will return True
# else, it will return False.
# the title of the function: def is_set_of_friends(arr)
#
# 2. Write a program that makes a friends list of random 20 items
# you must use the is_set_of_friends() function you created.

# 1.

import random


# def is_set_of_friends(arr):
#     if len(arr) % 2 != 0:
#         return False
#     checked_numbers = []
#     for i in range(len(arr)):
#         count = 0
#         checked = False
#         for j in range(len(checked_numbers)):
#             if arr[i] == checked_numbers[j]:
#                 checked = True
#         if not checked:
#             for k in range(i + 1, len(arr)):
#                 if arr[i] == arr[k]:
#                     count += 1
#             if count != 1:
#                 return False
#             checked_numbers.append(arr[i])
#     return True

# version 2
def is_set_of_friends(arr):
    for i in arr:
        if arr.count(i) != 2:
            return False
    return True
# 2.
# version 1:
# while True:
#     arr = []
#     for i in range(20):
#         num = random.randint(0,3)
#         arr.append(num)
#     if is_set_of_friends(arr):
#         break
# print(arr)

# version 2:
arr = []
def create_unique_item(arr):
    found = False
    while True:
        num = random.randint(0, 1000)
        for item in arr:
            if item == num:
                found = True
        if not found:
            arr.append(num)
            arr.append(num)
            break
        
        
# for i in range(10):
#     create_unique_item(arr)
# if is_set_of_friends(arr):
#     print(arr)