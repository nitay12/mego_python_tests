class Digit:
    def __init__(self, num):
        self.arr_digits = [0] * 10
        while num > 0:
            digit = num % 10
            self.arr_digits[digit] += 1
            num //= 10
    def equals(self, other):
    # V1
        for i in range(len(self.arr_digits)):
            if self.arr_digits[i] != other.arr_digits[i]:
                return False
        return True
    # V2
        # return self.arr_digits == other.arr_digits
    def compare_to(self, other):
        sum_digits_self = 0 
        sum_digits_other = 0
        for i in range(10):
            sum_digits_self += self.arr_digits[i]
            sum_digits_other += other.arr_digits[i]
        if sum_digits_self > sum_digits_other:
            return 1
        elif sum_digits_self < sum_digits_other:
            return 2
        else:
            self_index = 0
            other_index = 0
            self_digits_c = 0
            other_digits_c = 0
            for i in range(10):
                if self.arr_digits[i] != 0:
                    self_index = i
                    self_digits_c += 1
                    
                if other.arr_digits[i] != 0:
                    other_index = i
                    other_digits_c += 1
            if other_digits_c != 1 or self_digits_c != 1:
                return 0
            else:
                if self_index > other_index:
                    return 1
                else:
                    return 2


dig1 = Digit(245566)
dig2 = Digit(245566)
dig3 = Digit(45566999)
print(dig1.equals(dig2))
print(dig1.equals(dig3))