#codewars "Abbreviate a Two Word Name" Python

def abbrev_name(name):
    a = name[name.find(" ")+1].capitalize()
    return(name[0].capitalize()+"."+a)
