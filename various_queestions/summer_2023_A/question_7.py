class Coffee:
    def __init__(self, name, kind, strength, price):
        self.name = name
        self.kind = kind
        self.strength = strength
        self.price = price


def same_product(crr):
    for i in range(len(crr) - 1):
        if crr[i].name != crr[i + 1].name:
            return False
    return True


def weak_sorts(num, crr):
    arr = []
    for c in crr:
        if c.strength < num:
            if c.kind not in arr:
                arr.append(c.kind)
    return arr

def most_expensive(crr):
    # V1
    max_c = crr[0]
    for c in crr:
        if c.price > max_c.price:
            max_c = c
    print(max_c.name, max_c.price, max_c.strength, max_c.kind)

    # V2
    max_price = 0
    for c in crr:
        if c.price > max_price:
            max_price = c.price
    for c in crr:
        if c.price == max_price:
            print(max_c.name, max_c.price, max_c.strength, max_c.kind)