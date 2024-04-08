import random

sum_nums = 0
for i in range(39):
    num = random.randint(100, 999)
    print("num:", num)

    sum_nums += num

    if num % 2 == 0:
        sum = 0
        for i in range(3):
            sum += num % 10
            num = num // 10
        print("even, sum digits:", sum)
print("avg: ", sum_nums / 39)
