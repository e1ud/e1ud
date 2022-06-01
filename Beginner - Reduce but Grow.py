#codewars 'Beginner - Reduce but Grow' Python

def grow(arr):
    a = 1
    arr.sort()
    for i in arr:
        a = a * i
    return a
  
  
