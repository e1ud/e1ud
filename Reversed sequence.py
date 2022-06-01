#codewars 'Reversed sequence' Python

def reverse_seq(n):
    a = []
    for i in range(n, 0, -1):
        a.append(i)
    return a
