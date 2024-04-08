def count_blocks(arr, num):
    count_b = 0
    counter = 1
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            if counter >= num:
                count_b += 1
            counter = 1
        else:
            counter += 1
    if counter >= num:
                count_b += 1
    return count_b


