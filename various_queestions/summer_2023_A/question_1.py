for i in range(1, 1001):
    digit_sum = 0
    temp = i
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    if i % digit_sum == 0:
        print(i)
