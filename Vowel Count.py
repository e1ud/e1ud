#codewars 'Vowel Count' Python

def get_count(sentence):
    g = ["a", "e", "i", "o", "u"]
    b = 0
    for i in sentence:
        if i in g:
            b += 1
    return b
