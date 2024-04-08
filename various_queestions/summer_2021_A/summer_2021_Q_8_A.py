class Gift:
    def __init__(self, code, price, type):
        self.code = code
        self.price = price
        self.type = type

    # A
    def set_type(self, type):
        if type == "M" or type == "F" or type == "U" or type == "K":
            self.type = type

    # B
    def is_for_man(self):
        return self.type == "M" or self.type == "U"


# C V1
# def gift_check(arr, sum):
#     gifts = []
#     for gift in arr:
#         if gift.is_for_man() and gift.price == sum:
#             gifts.append(gift.code)
#     if len(gifts) >= 3:
#         for code in gifts:
#             print(code)

watch_gift = Gift(123, 300, "M")
print(watch_gift.type)
print(watch_gift.is_for_man())
watch_gift.set_type("F")
print(watch_gift.type)
print(watch_gift.is_for_man())


# C V2
def gift_check(arr, sum):
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if arr[i].price + arr[j].price + arr[k].price == sum:
                    print(arr[i].code, arr[j].code, arr[k].code)


arr = [
    Gift(1, 50, "M"),
    Gift(2, 20, "M"),
    Gift(3, 10, "M"),
    Gift(4, 30, "M"),
    Gift(5, 30, "M")
]

gift_check(arr, 80)