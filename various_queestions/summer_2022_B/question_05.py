class Country:
    def __init__(self, name, infected, recovered, dead):
        self.name = name
        self.infected = infected
        self.recovered = recovered
        self.dead = dead


class Status:
    def __init__(self):
        self.count1 = 0
        self.count2 = 0
        self.names = ""


def world_status(arr):
    count1 = 0
    count2 = 0
    names = ""
    for c in arr:
        c: Country
        if c.infected == 0:
            count1 += 1
        elif c.infected / 2 < c.recovered:
            names += f"{c.name} ,"
        if c.recovered > c.dead:
            count2 += 1
    s = Status()
    s.count1 = count1
    s.count2 = count2
    s.names = names
    return s


# TESTS
c1 = Country("Israel", 0, 0, 0)
c2 = Country("USA", 5, 3, 2)
c3 = Country("China", 5, 3, 3)

s = world_status([c1, c2, c3])
print(s.count1, s.count2, s.names)
