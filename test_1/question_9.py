def is_divisible(s, k):
    part_size = len(s) // k
    for i in range(0, len(s), part_size):
        if s[i:i + part_size] != s[:part_size]:
            return False 

    return True 