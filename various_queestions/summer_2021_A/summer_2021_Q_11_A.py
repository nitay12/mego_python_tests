def intersect(b, c):
    a = []
    for i in b:
        for j in c:
            if i==j:
                if i not in a:
                    a.append(i)
    return a

def are_strangers(a,b):
    return len(intersect(a,b)) == 0

print(are_strangers([1,2,3],[4,5,6]))
print(are_strangers([1,2,3,4],[4,5,6]))