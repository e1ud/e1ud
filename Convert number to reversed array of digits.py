#codewars "Convert number to reversed array of digits" python
def digitize(n):
    a = [int(x) for x in str(n)]
    a.reverse()
    return a
