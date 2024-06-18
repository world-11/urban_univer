from math import inf

def true_divide (first, second):
    res = 1.0
    if second == 0:
        res = inf
    else:
        res = first / second
    return res