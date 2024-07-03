# A v1
def exchange(number):
    while number > 0:
        if number < 10:
            return True
        if (number % 10) % 2 == (number // 10 % 10) % 2:
            return False
        number //= 10
    return True
# A v2
def exchange(num):
    if num < 10:
        return True
    string = str(num)
    for i in range(len(string)-1):
        if int(string[i]) % 2 == int(string[i + 1]) % 2:
            return False
    return True

# B v1
def min_exchange_d_sum(arr): 
    def d_sum(num):
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        return sum
    
    min_sum = -1
    index = -1
    for i in range(len(arr)):
        if exchange(arr[i]):
            dsum = d_sum(arr[i])
            if dsum < min_sum or min_sum == -1:
                index = i
                min_sum = dsum
    return index
# B v2
def min_exchange_d_sum(arr):
    min_dsum = float("inf")
    index = -1
    for i in range(len(arr)):
        if exchange(arr[i]):
            d_sum = 0
            for digit in str(arr[i]):
                d_sum += int(digit)
            if d_sum < min_dsum:
                min_dsum = d_sum
                index = i
    return index

print(min_exchange_d_sum([16, 33, 14, 567]))