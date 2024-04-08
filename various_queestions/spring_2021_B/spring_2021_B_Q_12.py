class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"

    def equals(self, other):
        return (
            self.day == other.day
            and self.month == other.month
            and self.year == other.year
        )

    def before(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day < other.day:
                    return True

        return False


class FoodItem:
    def __init__(
        self,
        name,
        quantity,
        production_date,
        expiry_date,
        min_temperature,
        max_temperature,
        price,
    ):
        self.name = name
        self.quantity = quantity
        self.production_date = production_date
        self.expiry_date = expiry_date
        self.min_temperature = min_temperature
        self.max_temperature = max_temperature
        self.price = price

    def is_fresh(self, d):
        if self.production_date.before(d) and d.before(self.expiry_date):
            return True
        else:
            return False

    def how_many_items(self, sum):
        qty = sum // self.price
        if qty <= self.quantity:
            return qty
        return self.quantity


fi1 = FoodItem("Pasta", 2, Date(21, 5, 2024), Date(21, 6, 2024), -40, 35, 10)
print(fi1.is_fresh(Date(24, 5, 2024)))
print(fi1.is_fresh(Date(24, 8, 2024)))
print(fi1.how_many_items(15))
print(fi1.how_many_items(40))


class Stock:
    def __init__(self):
        self.stock = []
        self.num_of_items = 0

    def how_many_items(self, temp):
        counter = 0
        for item in self.stock:
            if item.min_temperature < temp < item.max_temperature:
                counter += item.quantity
        return counter

    def remove_after_date(self, d):
        i = 0
        while i < len(self.stock):
            if self.stock[i].expiry_date.before(d):
                self.stock.pop(i)
            else:
                i += 1


fi2 = FoodItem("Pasta", 2, Date(21, 5, 2024), Date(21, 6, 2024), -40, 35, 10)
fi3 = FoodItem("Yogurt", 2, Date(21, 5, 2024), Date(21, 6, 2024), -40, 35, 10)
fi4 = FoodItem("Cheese", 2, Date(21, 5, 2024), Date(21, 6, 2024), -40, 35, 10)
fi5 = FoodItem("Orange Juice", 2, Date(21, 5, 2024), Date(21, 6, 2024), -40, 35, 10)
s1 = Stock()
s1.stock = [fi1, fi2, fi3, fi4, fi5]
print(s1.how_many_items(30))
print(s1.how_many_items(-50))
s1.remove_after_date(Date(1,1,2025))
print(s1.stock)