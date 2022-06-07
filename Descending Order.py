#codewars 'Descending Order' Python

def descending_order(num):
    a = []
    for i in str(num):
        a.append(i)
    a.sort(reverse=True)
    b = ""
    for i in a:
        b = b + i
    return int(b)
  

"""
Ok appearently there's much better and shorter way to do this, here's the code:

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
   
!!!NOT MINE
"""
