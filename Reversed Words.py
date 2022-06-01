#codewars 'Reversed Words' Python

def reverse_words(s):
    a = s.split()
    a.reverse()
    return (" ".join(a))
