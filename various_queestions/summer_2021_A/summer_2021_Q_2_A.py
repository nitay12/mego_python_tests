class Garbage:
    def __init__(self, location, quantity, capacity):
        self.location = location
        self.quantity = quantity
        self.capacity = capacity

def ready_to_empty(arr):
    to_empty = []
    for can in arr:
        if can.quantity / can.capacity > 0.5:
            to_empty.append(can.location)
    return to_empty

