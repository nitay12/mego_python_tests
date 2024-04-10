class Subject:
    def __init__(self, works, points, pass_grade):
        self.works = works
        self.points = points
        self.pass_grade = pass_grade
    def get_points(self, num_of_works, grade):  
        if self.pass_grade <= grade and num_of_works >= self.works/2:
            return self.points
        return 0

algo_sub = Subject(7, 3, 70)
oop_sub = Subject(4, 4, 60)
print(algo_sub.get_points(4,80))
print(algo_sub.get_points(3,80))
print(algo_sub.get_points(4,60))

def result(arr):
    sum_points = 0
    for sub in arr:
        works = int(input("Enter num of works"))
        grade = int(input("Enter grade"))
        points = sub.get_points(works, grade)
        sum_points += points
    return sum_points

print(result([algo_sub, oop_sub]))