#codewars 'Is he gonna survive?' Python

def hero(bullets, dragons):
    if bullets >= dragons*2:
        return True
    else:
        return False
        
#or 

def hero(bullets, dragons):
    return bullets >= dragons * 2
