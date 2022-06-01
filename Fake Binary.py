#codewars 'Fake Binary' Python

def fake_bin(x):
    y = ''
    for i in x:
        if int(i) < 5:
            y += "0"
        if int(i) >= 5:
            y += "1"
    return y
