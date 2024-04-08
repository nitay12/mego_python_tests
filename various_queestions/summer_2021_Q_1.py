sum = 0
arr = []
for i in range(35):
    num = int(input())
    sum += num
    arr.append(num)
avg = sum / 35
for num in arr:
    if num > avg:
        print(num)
        