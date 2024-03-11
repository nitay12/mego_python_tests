class Ball:
    def __init__(self, color, size, material):
        self.color = color
        self.size = size
        self.material = material


class BallPack:
    def __init__(self, num, cols, min_size, mat):
        self.balls = [None] * num
        self.colors = cols
        self.num_of_balls = 0
        self.min_size = min_size
        self.material = mat

    def is_fit(self, b):
        if b.material == self.material and b.size >= self.min_size and b.color in self.colors:
            return True
        else:
            return False
    
    def add(self, b):
        if self.is_fit(b):
            for i in range(len(self.balls)):
                if self.balls[i] == None:
                    self.balls[i] = b
                    return True
        return False

    def count_color (self, color):
        count = 0
        for ball in self.balls:
            if ball.color == color:
                count += 1
        return count

    def missing_colors (self):
        mis_cols_arr = []
        for ball in self.balls:
            if ball.color not in self.colors:
                mis_cols_arr.append(ball.color)
        if len(mis_cols_arr) > 0:
            return mis_cols_arr
        else:
            return None