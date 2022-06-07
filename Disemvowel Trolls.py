#codewars 'Disemvowel Trolls' Python

def disemvowel(string_):
    a = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    b = ""
    for i in string_:
        if i not in a:
            b = b+i
    return b
  
  
