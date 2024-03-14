i = 0
odd_count = 0
even_count = 0

while i < 4:
    num = int(input("Enter a whole positive number: "))
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    if 99 < num < 1000:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        print(digit_sum)
    i += 1
print("odds count: ", odd_count, ", even count: ", even_count)