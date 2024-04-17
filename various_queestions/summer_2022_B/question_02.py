def what(arr):
    m = 0
    for i in range(len(arr)):
        m1 = (m+arr[i]) / 2.0
        m2 = abs((m-arr[i]) / 2.0)
        m = m1 + m2
        print("i", i)
        print("arr[i]", arr[i])
        print("m1", m1)
        print("m2", m2)
        print("m", m)
    return m

print(what([4, 12, 8, 2, 6]))