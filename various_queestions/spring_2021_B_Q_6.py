def what(n1, n2):
    while n2>9:
        n2 = n2 / 10
    if n1 % 10 == n2:
        return True
    return False


n1 = int(input())
ok = True
n2 = None
count = 1
while ok:
    n2 = int(input())
    count += 1
    ok = what(n1, n2)
    n1 = n2
print(count)
