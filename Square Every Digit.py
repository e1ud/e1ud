#codewars 'Square Every Digit' Python

def square_digits(num):
    s = ""
    for i in str(num):
        y = int(i) * int(i)
        s = s + str(y) 
    return int(s)
