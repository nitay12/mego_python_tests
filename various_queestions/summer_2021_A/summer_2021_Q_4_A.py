arr = [1,4,6,11,12,9,2]
def is_up_down(arr):
    if arr[0] > arr[1]:
        return -1
    max_index = 0
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            max_index = i+1
        else:
            break
    for i in range(max_index, len(arr)-1):
        if arr[i] < arr[i+1]:
            return -1
    return max_index
print(is_up_down(arr))

# complexity = O(n) because the program is iterating over the data only once.
