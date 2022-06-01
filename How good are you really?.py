#codewars 'How good are you really?' Python

def better_than_average(class_points, your_points):
    a = 0
    g = len(class_points)
    for i in class_points:
        a = a + i
    b = a/g
    if b < your_points:
        return True
    else:
        return False
