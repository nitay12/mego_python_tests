# Write a python program that takes whole numbers until it gets the number 500
# The program needs to:
# 1. Print for each odd number's sum of digits
# 2. Calculate and print the average value of all the given numbers

# Solution v1:
numbers_sum = 0
numbers_count = 0
while True:
    input_number = int(input("Enter a whole number (or 500 to stop): "))
    if input_number == 500:
        print("Average of all numbers: ", (numbers_sum / numbers_count))
        break
    numbers_sum += input_number
    numbers_count += 1
    if input_number %2 != 0:
        sum = 0
        for digit in str(input_number):
            sum += int(digit)
        print("Digits sum: ", sum)