#codewars "Beginner Series #2 Clock" Python

def past(h, m, s):
    a = h * 3600000
    b = m * 60000
    c = s * 1000
    d = a + b + c
    return d
