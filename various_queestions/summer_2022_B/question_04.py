class Actor:
    def __init__(self, name, age, num_acts):
        self.name = name
        self.age = age
        self.num_acts = num_acts


class Act:
    def __init__(self, act_name, length):
        self.act_name = act_name
        self.length = length
        self.act_arr = []
        self.current_num = 0
    def add(self, actor):
        if self.current_num == 20:
            return "no room"
        elif actor.age < 45 or actor.num_acts < 5:
            return "not suitable"
        else:
            self.act_arr.append(actor)
            self.current_num += 1
            return "was added"

# TESTS
# Adding 19 valid actors to one Act
a1 = Act("Act one", 90)
for i in range(19):
    print(a1.add(Actor("actor", 56, 6)))
print("Number of current actors: ", a1.current_num)
# Trying to add not valid actors
    # Too young:
actor1 = Actor("Bob", 23, 6)
print(a1.add(actor1))
    # Not enough acts:
actor2 = Actor("Chris", 65, 3)
print(a1.add(actor2))
# No room
for i in range(3):
    print(a1.add(Actor("actor", 57, 10)))