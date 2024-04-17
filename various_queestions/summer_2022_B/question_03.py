def is_peak(index, arr):
    if arr[index] > arr[index-1] and arr[index] > arr[index+1]:
        return True
    return False

def num_of_peaks(arr):
    counter = 0
    for i in range(1, len(arr)-1):
        if is_peak(i, arr):
            counter += 1
    return counter
# Tests
print(is_peak(2,[1,2,3,4,5]))
print(is_peak(2,[1,4,7,4,5]))
print(num_of_peaks([1,2,1,5,6,7,5]))
print(num_of_peaks([1,2,3,4,5]))
