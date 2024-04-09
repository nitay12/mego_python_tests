# A
def exchange(number):
    if number < 10:
        return True
    while number > 0:
        if (number % 10) % 2 == (number // 10 % 10) % 2:
            return False
        number //= 10
    return True


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

print(min_exchange_d_sum([16, 33, 14, 567]))