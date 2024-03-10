# Write a python program that takes whole numbers until it gets the number 500
# The program needs to:
# 1. Print for each odd number's sum of digits
# 2. Calculate and print the average value of all the given numbers

# Solution v1:
# numbers_sum = 0
# numbers_count = 0
# while True:
#     input_number = int(input("Enter a whole number (or 500 to stop): "))
#     if input_number == 500:
#         print("Average of all numbers: ", (numbers_sum / numbers_count))
#         break
#     numbers_sum += input_number
#     numbers_count += 1
#     if input_number %2 != 0:
#         sum = 0
#         for digit in str(input_number):
#             sum += int(digit)
#         print("Digits sum: ", sum)

# Solution v2
input_number = 0
numbers_sum = 0
arr = []
while input_number != 500:
    input_number = int(input("Enter a whole number (or 500 to stop): "))
    arr.append(input_number)
    numbers_sum += input_number
    odd_sum = 0
    if input_number%2 != 0:
        while input_number != 0:
            odd_sum += input_number%10
            input_number = input_number//10
        print(odd_sum)
print(numbers_sum/len(arr))