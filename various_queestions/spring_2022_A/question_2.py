import random
def create_random_list(num):
    arr = []
    while len(arr) < num:
        rand = random.randint(10, 99)
        if rand %  10 > rand // 10:
            arr.append(rand)
    return arr

print(create_random_list(5))