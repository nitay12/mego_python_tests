def max_brother(arr1, arr2):
    max_value = 0
    max_value_index = 0
    for i in range(len(arr1)):
        brothers_count = 0
        d_sum = 0
        num = abs(arr1[i])
        while num > 0:
            d_sum += num % 10
            num //= 10
        for num2 in arr2:
            d2_sum = 0
            num2 = abs(num2)
            while num2 > 0:
                d2_sum += num2 % 10
                num2 //= 10
            if d_sum == d2_sum:
                brothers_count += 1
        if max_value < brothers_count:
            max_value = brothers_count
            max_value_index = i
    return max_value_index
