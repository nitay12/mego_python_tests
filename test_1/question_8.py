def what(arr):
    i = 0
    j = len(arr)-1
    while i < j:
        if arr[i] <= 0:
            i += 1
        elif arr[j] > 0:
            j -= 1
        else:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

def why(arr):
    new_arr = [0] * len(arr)
    ind = 0
    for i in range(len(arr)):
        if arr[i] <= 0:
            new_arr[ind] = arr[i]
            ind += 1
    for i in range(len(arr)):
        if arr[i] > 0:
            new_arr[ind] = arr[i]
            ind += 1
    for i in range(len(arr)):
        arr[i] = new_arr[i]

what_arr = [-8, 15, -15, 45, 123]
why_arr = [67, -46, 0, 55, -12]
what(what_arr)
print(what_arr)
why(why_arr)
print(why_arr)