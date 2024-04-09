# def is_copy_k(s1, s2):
    # if len(s1) % len(s2) != 0:
    #     return False
    # start = 0
    # end = len(s2)
    # i = len(s1) // len(s2)
    # for _ in range(i):
    #     if s1[start:end] != s2:
    #         return False
    #     start += len(s2)
    #     end += len(s2)
    # return True

    
    
def is_copy_k(s1, s2):
    i = len(s1) // len(s2)
    return s2 * i == s1
s1 = "AAA"
s2 = "A"
print(is_copy_k(s1, s2))